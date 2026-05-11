import requests
import json


def jprint(obj):
    """Print JSON data in a readable format."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get("http://api.open-notify.org/astros")

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    jprint(data)
else:
    print("There was an error connecting to the API.")