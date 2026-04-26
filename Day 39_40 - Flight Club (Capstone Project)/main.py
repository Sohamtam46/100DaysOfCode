from data_manager import DataManager
from flight_search import FlightSearch
from datetime import date,timedelta
from notification_manager import NotificationManager



# setup
data_manager = DataManager()
destination_list = data_manager.destination_data()
user_data = data_manager.get_customer_data()
user_email_list = [row['yourEmailAddress'] for row in user_data]
DEPARTURE_ID = "DUB" # Flights from Dublin
flight_search = FlightSearch(DEPARTURE_ID)
notification_manager = NotificationManager()


# getting today's date to determine the required dates for flight search
today = date.today()
# start date being tomorrow
dt = today + timedelta(days=1)
departure_arrival_dates = {}
# create a dict with outbound dates starting from tomorrow till 1 months.
# each date is 10 days apart for outbound dates
# return dates are 7 days apart.
# dict structure - {departure_date:[arrival_date1,date2,date3]}
for _ in range (3):
    departure_arrival_dates[str(dt)] = [str(dt + timedelta(days=i * 7)) for i in range(1, 4)]
    dt += timedelta(days=10)

for destination in destination_list:
    lowest_price = destination["lowestPrice"]
    print(destination["iataCode"])
    for outbound_date,return_dates in departure_arrival_dates.items():
        for return_date in return_dates:
            flight_information = flight_search.search_flight(destination["iataCode"],outbound_date,return_date,is_direct=True)
            try :
                flight_information["price_insights"]['lowest_price']
            except KeyError:
                print("---No Direct Flights---")
                print("---Looking for Indirect Flights---")
                flight_information = flight_search.search_flight(destination["iataCode"], outbound_date, return_date,
                                                                 is_direct=False)
            if lowest_price > flight_information["price_insights"]['lowest_price']:
                lowest_price = flight_information["price_insights"]['lowest_price']
                lowest_price_outbound_date = outbound_date
                lowest_price_return_date = return_date
                # print(len(flight_information["best_flights"][0]['flights']))
                nr_stops = len(flight_information["best_flights"][0]['flights']) - 1
                print(nr_stops)
    if lowest_price < destination["lowestPrice"]:
        print(lowest_price_outbound_date)
        print(lowest_price_return_date)
        destination["lowestPrice"] = lowest_price
        data_manager.update_lowest_price(lowest_price, destination["id"])

        message_data = [lowest_price,
                        destination["iataCode"],
                        lowest_price_outbound_date,
                        lowest_price_return_date,
                        nr_stops]
        notification_manager.send_message(message_data)
        for emails in user_email_list:
            notification_manager.send_email(emails,message_data)









