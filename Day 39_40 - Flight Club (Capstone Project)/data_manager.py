import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.google_sheet_endpoint = "https://api.sheety.co/1a4a784652e4f265dc78e101da3699c5/flightPrices/prices"
        self.headers = {
            "Authorization": os.getenv("SHEETY_API_KEY")
        }
        self.fetch_data()

    def destination_data(self):
        return [destination_data for destination_data in self.current_lowest_flight_price_data['prices']]


    def fetch_data(self):
        print("File fetched")
        response = requests.get(url=self.google_sheet_endpoint, headers=self.headers)
        response.raise_for_status()
        self.current_lowest_flight_price_data = response.json()

    def update_lowest_price(self,lowest_price,destination_id):
        print(f"Lowest price : {lowest_price}")
        google_sheet_endpoint_update = f"{self.google_sheet_endpoint}/{destination_id}"
        row_data = {
            "price":{
                "lowestPrice": lowest_price
            }
        }
        requests.put(url=google_sheet_endpoint_update,json=row_data, headers=self.headers)
        print("File written")
        print("Successfully")
        self.fetch_data()

    def get_customer_data(self):
        users_sheety_endpoint = "https://api.sheety.co/1a4a784652e4f265dc78e101da3699c5/flightPrices/users"
        response = requests.get(url=users_sheety_endpoint, headers=self.headers)
        response.raise_for_status()
        user_data = response.json()
        return user_data["users"]






