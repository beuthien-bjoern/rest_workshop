import requests

# TODO(beuthien): Prettify this file
banner_json = '{"Cisco-IOS-XE-native:banner": {"login": {"banner": "Geaendert"}}}'
headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json'
    }
response = requests.put('https://10.202.10.254/restconf/data/Cisco-IOS-XE-native:native/banner', data=banner_json,
                        auth=('cisco', 'cisco'),
                        headers=headers,
                        verify=False)
print(f'Status code: {response.status_code}')
print('banner ' + response.text)
