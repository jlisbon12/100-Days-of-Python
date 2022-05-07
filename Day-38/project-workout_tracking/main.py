import requests
from datetime import datetime

APP_ID = "f879c1b0"
API_KEY = "b4a2ac15fe6b9462a5c336d745d307e9"

USER_GENDER = "female"
USER_WEIGHT = "55"
USER_HEIGHT = "170"
USER_AGE = "20"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": input("Tell what exercise you did today: "),
    "gender": USER_GENDER,
    "weight_kg": USER_WEIGHT,
    "height_cm": USER_HEIGHT,
    "age": USER_AGE
}

response = requests.post(url=f"{api_endpoint}", json=exercise_config, headers=headers)
result = response.json()


sheety_endpoint = "https://api.sheety.co/1cda47ec0399a6041f93b2ea32157e1e/myWorkouts2022/workouts"
today = datetime.now()

sheety_headers = {
    "Authorization": "Basic SmVkYWU6bnNpdkVvc29iSGxw"
}

for i in range(0, len(result['exercises'])):
    sheety_config = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": f"{result['exercises'][i]['name'].title()}",
            "duration": f"{result['exercises'][i]['duration_min']}",
            "calories": f"{result['exercises'][i]['nf_calories']}"
        }
    }

    sheety_response = requests.post(url=f"{sheety_endpoint}", json=sheety_config, headers=sheety_headers)
