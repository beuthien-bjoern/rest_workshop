import requests

# TODO(beuthien): Prettify this file
banner_json = '{"Cisco-IOS-XE-native:banner": {"login": {"banner": "Willkommen in der Hölle" } } }'
headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
response = requests.put('https://10.214.13.254/restconf/data/Cisco-IOS-XE-native:native/banner', data=banner_json,
                        auth=('cisco', 'cisco'),
                        headers=headers,
                        verify=False)
print(f'Status code: {response.status_code}')
print('banner ' + response.text)
