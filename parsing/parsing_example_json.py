import json

with open("person.json", mode="r", encoding="utf-8") as read_file:
    person_data = json.load(read_file)
    for person in person_data:
        if person["vorname"] == 'Anna':
            print('Hey, Anna')
            person['adresse']['strasse'] = 'Neue Strasse'
            person['aktualisiert'] = 'updated'
        if person['vorname'] == 'David':
            person_data.remove(person)

    print(json.dumps(person_data))

