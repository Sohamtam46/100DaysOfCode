import os
import requests
from datetime import datetime

# checking server status
# response = requests.get(url="https://app.100daysofpython.dev/healthz")
# print(response.text)

#
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
TOKEN = os.environ.get("TOKEN")

# getting data from server
nl_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json'
}
query={
      "query": input("How much did you run today?"),
      "weight_kg": 80,                  # Optional: Weight in kg (1-500)
      "height_cm": 169,                 # Optional: Height in cm (1-300)
      "age": 26,                        # Optional: Age (1-150)
      "gender": "male"                  # Optional: "male" or "female"
}

nl_response = requests.post(nl_endpoint,json=query,headers=headers)
nl_response.raise_for_status()
data = nl_response.json()
calories = data["exercises"][0]["nf_calories"]
duration = data["exercises"][0]["duration_min"]
exercise_name= data["exercises"][0]["name"]


# Updating the exercise in Google sheets using sheety:
# google sheet - https://docs.google.com/spreadsheets/d/1RtxWJ6dV-aRrrEoekgLv1n7caa-cMs8oMeHWn7TyNBc/edit?gid=0#gid=0

google_sheet_endpoint = SHEET_ENDPOINT
today = datetime.now()
# output - 2026-04-20 06:57:26.030209
today_date = today.strftime("%d/%m/%Y")
run_start_time = today.strftime("%X")
headers = {
    "Authorization":TOKEN
}

sheety_query = {
    "workout":{
        "date": today_date,
        "time":run_start_time,
        "exercise":exercise_name.title(),
        "duration":duration,
        "calories":calories
    }
}

sheety_response = requests.post(url=google_sheet_endpoint,json=sheety_query,headers=headers)
print(sheety_response.text)


