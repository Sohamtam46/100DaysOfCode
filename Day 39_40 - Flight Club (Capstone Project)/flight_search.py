import requests_cache
from dotenv import load_dotenv
import os

# conserve request by caching the response. TTL - indefinite for testing
session = requests_cache.CachedSession('flight_cache')
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,departure_id):
        self.serpapi_endpoint = "https://serpapi.com/search?engine=google_flights"
        self.engine = "google_flights"
        self.departure_id = departure_id
        self.currency = "EUR"

    def search_flight(self,arrival_id,outbound_date,return_date,is_direct):
        if not is_direct:
            stops = 0 #indirect flight with no set number of layovers
        else:
            stops = 1

        query = {
            "api_key": os.getenv("SERP_API_KEY"),
            "engine": self.engine,
            "departure_id": self.departure_id,
            "arrival_id": arrival_id,
            "currency": self.currency,
            "type": "1",
            "outbound_date": outbound_date,
            "return_date": return_date,
            "stops": stops
        }
        response = session.get(url=self.serpapi_endpoint,params=query)
        response.raise_for_status()
        best_flight_data = response.json()

        return best_flight_data
