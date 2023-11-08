#Implementing the class library with all the json functions
import json 

#Creating a data set with key value pairs
data = {

    'name': 'Katie',
    'age': 29,
    'city': 'Seattle, WA',
    'interests': ['Shopping', 'Watching horror movies', 'Watching Kdramas'],
    'is_student': True

}

#Opening the data.json file with the file as one of the arguments and w for writing in the data as a json_file
with open('data.json', 'w') as json_file:
    #Using the json object to call on dump, to pass in all the data with key value in it and json_file as one of the arguments with an indentation of 4 spaces.
    json.dump(data, json_file, indent=4)

#Printing out the string Data has been written to data.json"
print('Data has been written to data.json')

#Opening the data.json file as a argument, passing in r to read the data.json file
with open('data.json', 'r') as json_file:
    #Creating a loaded_data variable
    #Using the json object to call on the load function, passing in the json_file to read the data.
    loaded_data = json.load(json_file)

#Prints out the string to say Data loaded from data.json
print('Data loaded from data.json')
#Prints out all of the data from the key value pair dataset
print(loaded_data)

#Changing the values in the data
loaded_data['age'] = 30
loaded_data['interests'].append('Watching Anime')

#Opening the data.json file and passing in the w to have these written dataset written
with open('data.json', 'w') as json_file:
    #Usingthe json object to call on the dump function to pass in the loaded_data, json_file, and indentation of 4 to have the new dataset be shown and entered.
    json.dump(loaded_data, json_file, indent=4)

#Prints out the string that says Modified data to the data.json file.
print("Modified data to the data.json file")