import requests
import json

#Get the response
response = requests.get("https://swapi.info/api/people/1")

#Print the response code
print("Status Code:", response.status_code)

#Formats the response if response is 200, else it prints the response code
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print("Error getting data from API.")
    print(response.text)