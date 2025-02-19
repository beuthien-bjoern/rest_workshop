import json
import requests
import urllib.parse
import urllib3

# Disable SSL warnings (for testing purposes)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Corrected payload structure
payload = {
  "Cisco-IOS-XE-native:Serial": {
    "name": "0/1/0",
    "ip": {
      "address": {
        "primary": {
          "address": "172.214.13.10",
          "mask": "255.255.255.0"
        }
      }
    }
  }
}


def request_put(endpoint):
    base_url = 'https://10.214.13.254'
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    authentication = ('cisco', 'cisco')

    request_url = base_url + endpoint
    response = requests.put(request_url,
                            headers=headers,
                            auth=authentication,
                            data=json.dumps(payload),
                            verify=False)

    print(f'PUT request to {request_url}\nStatus Code: {response.status_code}')
    print(response.text)
    return response

if __name__ == '__main__':
    # Keep your original interface encoding logic
    interface_in_url = urllib.parse.quote("0/1/0", safe='=')
    endpoint = f'/restconf/data/Cisco-IOS-XE-native:native/interface/Serial={interface_in_url}'

    response = request_put(endpoint)

    if response.status_code in [200, 204]:
        print("Successfully updated interface")
    else:
        print("Issue with updating interface")
