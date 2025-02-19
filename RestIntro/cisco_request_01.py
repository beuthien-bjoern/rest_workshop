import requests
import urllib

def request_get(endpoint):
    base_url = 'https://10.214.13.254'
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
    # Discover the root of the RESTCONF API, see https://datatracker.ietf.org/doc/html/rfc8040#section-3.1
    # After discovering the RESTCONF API root, the client MUST use this
    # value as the initial part of the path in the request URI, in any
    # subsequent request for a RESTCONF resource.
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

    # Again get information about a specific interface with the problem of '/' being in the
    # interface name. Thus we need to use escapes. Here, the quote function of urllib.parse helps us.
    # https://docs.python.org/3/library/urllib.parse.html
    interface_in_url = urllib.parse.quote("GigabitEthernet0/0/0", safe='=')
    endpoint = f'/restconf/data/ietf-interfaces:interfaces/interface={interface_in_url}'
    repsonse = request_get(endpoint)

    # Get information about the implemented YANG-types
    endpoint = '/restconf/data/ietf-yang-library:modules-state'
    response = request_get(endpoint)
