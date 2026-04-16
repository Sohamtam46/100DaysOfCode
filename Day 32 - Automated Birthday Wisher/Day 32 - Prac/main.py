import smtplib

MY_EMAIL = "test@test.com"
PASSWORD = "test"

import datetime as dt
import random
now = dt.datetime.now()

if now.weekday() == 1:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        quote_of_the_day = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs="test@gmail.com",
                            msg=f"Subject:Quote of the Day\n\n{quote_of_the_day}\nThank you!"
                            )

