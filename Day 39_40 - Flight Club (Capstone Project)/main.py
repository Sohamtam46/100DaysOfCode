#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import date,timedelta
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
# flight_data = FlightData()

today = date.today()
dt = today + timedelta(days=1)
departure_arrival_dates = {}
# create a dict with outbound dates starting from tomorrow till 3 months.
# each date is 10 days apart for outbound dates
# return dates are 7 days apart.
# dict structure - {departure_date:[arrival_date1,date2,date3]}
for _ in range (9):
    departure_arrival_dates[str(dt)] = [str(dt + timedelta(days=i * 7)) for i in range(1, 4)]
    dt += timedelta(days=10)
#
for destination in data_manager.response['prices']:
    for outbound_date,return_dates in departure_arrival_dates.items():
        for return_date in return_dates:
            flight_information = flight_search.search_flight(destination["iataCode"],outbound_date,return_date)
            if destination["lowestPrice"] > flight_information[0]['price']:
                data_manager.update_lowest_price(flight_information[0]['price'],destination["id"])





