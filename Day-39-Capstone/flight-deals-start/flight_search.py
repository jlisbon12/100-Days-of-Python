import requests
from flight_data import FlightData

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_code(self, city_term):
        flight_endpoint = "https://tequila-api.kiwi.com"

        headers = {
            "apikey": "nuOuPtFyRwSEPpaHk2upw1QoVGaOJs0d"
        }

        flight_param = {
            "term": city_term,
            "locale": "en-US",
            "location-types": "airport"
        }

        response = requests.get(url=f"{flight_endpoint}/locations/query", params=flight_param,
                                     headers=headers)
        result = response.json()
        return result['locations'][0]['code']

    def check_flight(self, origin_city_code, dest_city_code, time_from, time_to):
        flight_endpoint = "http://tequila-api.kiwi.com/v2/search"
        header = {
            "apikey": "Mn4t6i8IsLpwiJUccjRlRu_H7RB7w01J"
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": dest_city_code,
            "date_from": time_from.strftime("%d/%m/%Y"),
            "date_to": time_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": 0
        }
        response = requests.get(url=f"{flight_endpoint}", params=query, headers=header)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No Key Found for {dest_city_code}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            dest_city=data["route"][0]["cityTo"],
            dest_airport=data["route"][0]["flyTo"],
            leave_date=data["route"][0]["local_departure"].split("T")[1],
            return_date=data["route"][0]["local_departure"].split("T")[0])

        print(f"{flight_data.dest_city}: ${flight_data.price}")
        return flight_data

