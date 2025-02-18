import xml.etree.ElementTree as ET
import copy

tree = ET.parse('xml_to_parse.xml')
root = tree.getroot()

print(root.tag)

namespaces = {"Cisco": "http://cisco.com/ns/yang/Cisco-IOS-XE-native"} 

for interface in root.findall('Cisco:GigabitEthernet',namespaces=namespaces):
    print(interface.tag)
    
    if interface.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}name').text == '0/0/0':
        print('gefunden')
        ip = interface.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}ip')
        address = ip.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}address').find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}primary').find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}address')
        print(address.text)
    if interface.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}name').text == '0/0/1':
        ip2 = copy.deepcopy(ip)
        #interface.append(ip2)
        interface.insert(1, ip2)
        address = interface.find('Cisco:ip',namespaces=namespaces).find('Cisco:address',namespaces=namespaces)
        primary = address.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}primary')
        ip_address = primary.find('{http://cisco.com/ns/yang/Cisco-IOS-XE-native}address')
        ip_address.text = '192.168.214.1'
ET.dump(tree)