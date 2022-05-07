import requests
from flight_search import FlightSearch

sheety_endpoint = "https://api.sheety.co/1cda47ec0399a6041f93b2ea32157e1e/flightDeals2022/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def get_info(self):
        response = requests.get(url=f"{sheety_endpoint}")
        result = response.json()
        self.data = result['prices']
        return self.data

    def add_code(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )

