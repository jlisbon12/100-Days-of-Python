#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY = "ATL"

data_manager = DataManager()
sheet_data = data_manager.get_info()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]['iataCode'] == " ":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_code(row['city'])
    data_manager.data = sheet_data
    data_manager.add_code()

day = datetime.now()
tomorrow = day + timedelta(days=1)
six_months = day + timedelta(days=(6 * 30))

for dest in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY,
        dest['iataCode'],
        time_from=tomorrow,
        time_to=six_months
    )

    if flight.price < dest["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low Price Alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.dest_city}-{flight.dest_airport}, from {flight.leave_date} to {flight.return_date}"
        )

