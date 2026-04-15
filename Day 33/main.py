import requests

# Response code
# 200 - OK
# 1XX: hold on
# 2xx: it works
# 3xx: no access
# 4xx: issue with fetch
# 5xx: server down

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_location = (longitude,latitude)

print(iss_location)