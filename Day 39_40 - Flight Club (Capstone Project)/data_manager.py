import requests
import requests_cache
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
        self.response = requests.get(url=self.google_sheet_endpoint,headers=self.headers)


    def update_lowest_price(self,lowest_price,destination_id):
        google_sheet_endpoint_update = f"{google_sheet_endpoint}/{destination_id}"
        row_data = {
            "price":{
                "lowestPrice": lowest_price
            }
        }
        requests.put(url=google_sheet_endpoint_update,json=row_data, headers=self.headers)




