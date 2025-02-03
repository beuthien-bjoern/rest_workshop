import requests

def request_get(endpoint):
    base_url = 'https://10.202.10.254'
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
    authentication = ('cisco', 'cisco')

    request_url = base_url + endpoint
    response = requests.get(request_url,
                            headers=headers,
                            auth=authentication,
                            verify=False)

    print(f'Get request to {request_url}\nstatus code: {response.status_code}')
    print(response.text)
    return response

if __name__ == '__main__':
    endpoint = '/.well-known/host-meta'
    response = request_get(endpoint)

    endpoint = '/restconf'
    response = request_get(endpoint)

    # Get information about the interfaces via cisco-ios-xe-native
    endpoint = '/restconf/data/Cisco-IOS-XE-native:native/interface'
    response = request_get(endpoint)

    # Again get information about the interfaces but this time with a different
    # YANG definition.
    endpoint = '/restconf/data/ietf-interfaces:interfaces'
    repsonse = request_get(endpoint)

    # Get information about the implemented YANG-types
    endpoint = '/restconf/data/ietf-yang-library:modules-state'
    response = request_get(endpoint)
