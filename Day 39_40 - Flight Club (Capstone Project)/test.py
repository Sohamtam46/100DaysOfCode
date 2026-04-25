import requests
# from datetime import date,timedelta
#
# today = date.today()
# dt = today + timedelta(days=1)
# departure_arrival_dates = {}
#
# for _ in range (9):
#     departure_arrival_dates[str(dt)] = [str(dt + timedelta(days=i * 7)) for i in range(1, 4)]
#     dt += timedelta(days=10)
#
# for outbound_date,return_dates in departure_arrival_dates.items():
#     pass
#
#
# test = [{'flights': [{'departure_airport':
#                    {'name': 'Dublin Airport', 'id': 'DUB', 'time': '2026-04-26 08:35'},
#                'arrival_airport':
#                    {'name': 'Heathrow Airport', 'id': 'LHR', 'time': '2026-04-26 10:10'},
#                'duration': 95,
#                'airplane': 'Airbus A320neo',
#                       'airline': 'British Airways',
#                'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/BA.png',
#                'travel_class': 'Economy',
#                'flight_number': 'BA 825',
#                       'ticket_also_sold_by': ['Aer Lingus'],
#                       'legroom': '29 in',
#                 'extensions': ['Below average legroom (29 in)', 'Wi-Fi for a fee', 'In-seat USB outlet',
#                               'Carbon emissions estimate: 55 kg']}],
#                 'total_duration': 95,
#                 'carbon_emissions': {'this_flight': 55000, 'typical_for_this_route': 59000, 'difference_percent': -7},
#                 'price': 150,
#                 'type': 'Round trip', 'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/BA.png',
#                 'departure_token': 'WyJDalJJZEcxNVluTnZkMDFVTkUxQlNWWlJiWGRDUnkwdExTMHRMUzB0TFc5clltWndNVUZCUVVGQlIyNXpWazlGUjB0d2QwZEJFZ1ZDUVRneU5Sb0tDTkIwRUFJYUEwVlZVamdjY051SUFRPT0iLFtbIkRVQiIsIjIwMjYtMDQtMjYiLCJMSFIiLG51bGwsIkJBIiwiODI1Il1dXQ=='}]
#
# print(f"price : {test[0]['price']}")

google_sheet_endpoint = "https://api.sheety.co/1a4a784652e4f265dc78e101da3699c5/flightPrices/prices/2"
headers = {
            "Authorization": "Basic c29oYW10YW00NkBnbWFpbC5jb206SXJlbGFuZEAyMDI2"
        }
row_data = {    
    "price":{
    "lowestPrice": 20
    }
}
response = requests.put(url=google_sheet_endpoint,json=row_data, headers=headers)