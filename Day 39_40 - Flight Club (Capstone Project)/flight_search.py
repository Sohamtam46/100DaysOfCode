import serpapi
import requests
import requests_cache
from dotenv import load_dotenv
import os

session = requests_cache.CachedSession('flight_cache')
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.serpapi_endpoint = "https://serpapi.com/search?engine=google_flights"
        self.engine = "google_flights"
        self.departure_id = "DUB"
        self.currency = "EUR"

    def search_flight(self,arrival_id,outbound_date,return_date):
        query = {
            "api_key": os.getenv("SERP_API_KEY"),
            "engine": self.engine,
            "departure_id": self.departure_id,
            "arrival_id": arrival_id,
            "currency": self.currency,
            "type": "1",
            "outbound_date": outbound_date,
            "return_date": return_date
        }
        response = session.get(url=self.serpapi_endpoint,params=query)
        response.raise_for_status()
        best_flight_data = response.json()
        return best_flight_data
