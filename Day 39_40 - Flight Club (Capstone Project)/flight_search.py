import serpapi
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT = serpapi.Client(api_key=os.getenv("SERP_API_KEY"))


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.engine = "google_flights"
        self.departure_id = "DUB"
        self.currency = "EUR"

    def search_flight(self,arrival_id,outbound_date,return_date):
        results = CLIENT.search({
            "engine": self.engine,
            "departure_id": self.departure_id,
            "arrival_id": arrival_id,
            "currency": self.currency,
            "type": "1",
            "outbound_date": outbound_date,
            "return_date": return_date
        })
        return results["best_flights"]