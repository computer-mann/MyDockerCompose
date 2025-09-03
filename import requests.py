import requests
import time

#url = "http://34.252.113.193:9090/api/customers"
url="http://localhost:5003/api/customers?count=1000"

while True:
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    time.sleep(1)  # Adjust the delay as needed to avoid overwhelming the server
