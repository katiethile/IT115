import json 

data = {

    'name': 'Katie',
    'age': 29,
    'city': 'Seattle, WA',
    'interests': ['Shopping', 'Watching horror movies', 'Watching Kdramas'],
    'is_student': True

}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Data has been written to data.json')

with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print('Data loaded from data.json')
print(loaded_data)

loaded_data['age'] = 30
loaded_data['interests'].append('Watching Anime')

with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print("Modified data to the data.json file")