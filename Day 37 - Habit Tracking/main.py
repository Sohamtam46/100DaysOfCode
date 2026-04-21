import requests
    from datetime import datetime

# https://pixe.la/@soham26
# api_docs = https://docs.pixe.la/

USERNAME = "soham26"
TOKEN = "test"
GRAPH_ID = "graph1"

# ----- creating a user -----
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":"test",
    "username":"soham26",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN":TOKEN
}

# ----- graph set-up -----
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

# response = requests.post(graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# ----- positing a pixel -----

pixel_addition_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_addition_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today?")
}
#
response = requests.post(pixel_addition_endpoint,json=pixel_addition_config,headers=headers)
print(response.text)

# ----- update a pixel -----

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260419"

update_pixel_config = {
    "quantity" : "10.23"
}

# response = requests.put(pixel_update_endpoint,json=update_pixel_config,headers=headers)
# print(response.text)

# ----- delete a pixel -----

pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20260417"
#
# response = requests.delete(pixel_deletion_endpoint,headers=headers)
# print(response.text)

