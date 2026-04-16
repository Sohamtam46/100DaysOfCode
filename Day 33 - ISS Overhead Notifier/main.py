
#  International Space Station Notifier
#  Soham, 15/4

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.286127
MY_LONG =-9.007699
MY_EMAIL = "test@test.com"
PASSWORD = "test"

# Response code
# 200 - OK
# 1XX: hold on
# 2xx: it works
# 3xx: no access
# 4xx: issue with fetch
# 5xx: server down

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Look Up: It's ISS!\n\nCheck the Sky, you can spot ISS."
                            )


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # fetching iss location
    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]
    # iss_location = (iss_longitude,iss_latitude)
    if (MY_LAT - 5 <= float(iss_latitude) <= MY_LAT + 5) or (MY_LONG - 5 <= float(iss_longitude) <= MY_LONG + 5):
        return True

def is_night_time():
    # Fetching the sunrise and sunset time according to my location to check nighttime
    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset_hour or time_now.hour <= sunrise_hour:
        return True

# keeps the program running and checks every 60 seconds
while True:
    time.sleep(60)
    if is_night_time() and iss_is_overhead():
        send_email()


