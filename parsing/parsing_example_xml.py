import xml.etree.ElementTree as ET

tree = ET.parse('person.xml')
root = tree.getroot()

print(root.tag)

# You can iterate through all direct children
for child in root:
    print(child.tag)

for person in root.findall('person'):
    if person.find('vorname').text == 'Anna':
        address = person.find('adresse')
        print(address.find('strasse').text)
        address.find('strasse').text = 'Neue Strasse'
        element = ET.Element('updated')
        element.text = 'yes'
        person.append(element)
    if person.find('vorname').text == 'David':
        root.remove(person)

ET.dump(tree)



