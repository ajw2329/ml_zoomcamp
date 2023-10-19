import requests
url = "http://localhost:9696/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}


print(round(requests.post(url, json=client).json()["credit_probability"], 3))