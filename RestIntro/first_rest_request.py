import requests

# Use Dungeons & Dragons API from https://5e-bits.github.io/docs/api
base_url = "https://www.dnd5eapi.co"

# Endpoint to get all spells. For other endpoints see API documentation
endpoint = "/api/spells"

# List header fields for the requests
headers = {
  # Media type that is acceptable for the response, here: JSON-data
  'Accept': 'application/json'
}

# Send the request
response = requests.get(base_url + endpoint, headers=headers)

print("Response with status code " + str(response.status_code))
print("Content type: " + response.headers["Content-Type"])
print(response.json())
