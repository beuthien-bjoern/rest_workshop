import requests

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

    