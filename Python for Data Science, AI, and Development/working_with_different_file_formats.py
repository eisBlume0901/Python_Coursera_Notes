import requests
import os
import pandas as pd
import numpy as np
import json
import xml.etree.ElementTree as ET
from PIL import Image

# csv file
url_1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
response = requests.get(url_1)
path = os.path.join(os.getcwd(), "addresses.csv")
with open(path, "wb") as file:
    file.write(response.content)

addresses_df = pd.read_csv("addresses.csv", header=None)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

print(addresses_df.head(3))

addresses_df.columns = ["First Name", "Last Name", "Location", "City", "State", "Area Code"]
print(addresses_df)
print(addresses_df[["First Name", "Last Name", "State"]])
print(addresses_df.iloc[[0, 1, 2]]["First Name"]) # rows, columns
print(addresses_df.iloc[[2][:]])

numbers_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"])
numbers_df = numbers_df.transform(func = lambda x : x + 10)
print(numbers_df)
numbers_df = numbers_df.transform(func = ["sqrt"])
print(numbers_df)


# json file
# json - collection of name/value pairs
# It is language-independent data format (derived from JavaScript)

person = {
    "firstName": "Mary Claire",
    "lastName": "Ethereal",
    "age": 25,
    "address": {
        "streetAddress": "901 Banana Apple Street",
        "city": "Delicious Fruits",
        "state": "Food",
        "postalCode": "BA901548-450"
    }
}

with open("person.json", "w") as f:
    json.dump(person, f) # dump() used for writing to JSON file

# Serializing json
json_object = json.dumps(person, indent = 4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)

# Serialization is the process of converting an object into a special format which is suitable for
# transmitting over the network or storing in file or database.

# dumps vs dump
# dumps - converts Python object into JSON string. Used when you want to serialize the object
# and keep the JSON data in memory, not write it to a file
# "in memory" = temporarily stored in the computer's RAM. When a program runs, it uses RAM to store
# variables, objects, and other data that it needs to access quickly and frequently.

# dump - converts a Python object into a JSON string and writes it to a file. Used when you want to serialize the object
# and save the JSON data to a file for later use
# In comparison with dumps, dump allows permamnent storage (as the data remains even after the program has finished
# running and the computer is turned off)

# Reading json file

# Deserialization converts the special format returned by the serialization back into a usable object
with open("sample.json", "r") as openfile:
    json_object = json.load(openfile)

print(json_object)
print(type(json_object)) # <class 'dict'>


# XML file
# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
fourth = ET.SubElement(details, 'job')
first.text = 'Emerald Dendron'
second.text = 'Greenleaf'
third.text = '25'
fourth.text = 'Data Scientist'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
response = requests.get(url_2)
path = os.path.join(os.getcwd(), "Sample-employee-XML-file.xml")
with open(path, "wb") as file:
    file.write(response.content)

tree = ET.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
print(root) # <Element 'employees' at 0x00000198730068E0>, look at the xml file it is <employees>
employee_df = pd.DataFrame(columns=["firstname", "lastname", "title", "division", "building", "room"])
employee_dict = []
for node in root:
    dict = {"firstname": None, "lastname": None, "title": None, "division": None, "building": None, "room": None}
    for key in dict:
        dict[key] = node.find(key).text
    employee_dict.append(dict)

print(employee_dict)
employee_df = pd.DataFrame(employee_dict)
print(employee_df.head(3))


# Binary File Format (like images)
url_3 = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"
response = requests.get(url_3)
path = os.path.join(os.getcwd(), "dog.jpg")
with open(path, "wb") as file:
    file.write(response.content)

dog_image = Image.open("dog.jpg", "r")
dog_image.show()