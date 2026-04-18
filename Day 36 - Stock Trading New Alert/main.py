from operator import truediv

import requests
from twilio.rest import Client


# ----------------------------CONSTANTS-----------------------------------------
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
PERCENTAGE_CHANGE_ALERT = 0.2

# ----------------------------ENV VARIABLES--------------------------------------
AV_API_KEY = "test"
NEWS_API_KEY = "test"
account_sid = "test"
auth_token = "test"
client = Client(account_sid, auth_token)

# -----------------------------------------------------------------------------------------------------------------
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def is_significant_price_change():
    global percentage_change

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
    }
    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
    #  i -> gives the index while .items() gives me the date:value in the dict
    #  i<2 condition is cause we need the first two dates data everyday
    last_two_days = {date: value for i, (date, value) in enumerate(data['Time Series (Daily)'].items()) if i < 2}
    last_two_days_closing_price = [round(float(value['4. close']), 2) for date, value in last_two_days.items()]
    # percentage = (388.9 - 391.95)/388.9 * 100 [negative means decrease, positive means increase]
    percentage_change = ((last_two_days_closing_price[0] - last_two_days_closing_price[1]) / last_two_days_closing_price[0]) * 100
    if abs(percentage_change) > PERCENTAGE_CHANGE_ALERT:
        print("There's change")
        return True
    else:
        print("There's no change")
        return False

# -----------------------------------------------------------------------------------------------------------------
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    parameters = {
            "q": COMPANY_NAME,
            "from": "2026-04-16",
            "sortBy": "popularity",
            "language":"en",
            "pageSize":3,
            "apiKey":NEWS_API_KEY
        }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    data = response.json()
    print("first 3 significant news fetched.")
    return data

def format_message(article):
    print("Message Formated")
    if percentage_change > 0 :
        change_emoji = "🔺"
    else:
        change_emoji = "🔻"

    return (f"{STOCK}:{change_emoji} {round(abs(percentage_change),2)}\n"
            f"Headline: {article["title"]}\n"
            f"Brief: {article["description"]}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_message(message):
    print("Message Sent")
    message = client.messages.create(
        from_="whatsapp:+test",
        body=f"{message}",
        to='whatsapp:+test'
    )

if is_significant_price_change():
    data = get_news()
    for article in data["articles"]:
        formated_message = format_message(article)
        send_message(formated_message)






# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
