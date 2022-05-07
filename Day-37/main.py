import requests
from datetime import datetime
from datetime import timedelta

TOKEN = "qwesdfytrcvboiumnbh"
USERNAME = "jedaelisbon"
ID = "graph1"

api_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(api_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "mins",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{ID}"
today = datetime.now()

THIS_DAY = today.strftime("%Y%m%d")

pixel_config = {
    "date": THIS_DAY,
    "quantity": input("How many minutes have you been coding?\n")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)


update_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{ID}/{THIS_DAY}"

update_config = {
    "quantity": "75"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

del_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{ID}/{THIS_DAY}"

# response = requests.delete(url=del_endpoint, headers=headers)
# print(response.text)
