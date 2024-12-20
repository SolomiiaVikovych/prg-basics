basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {}

for key,value in basic_data.items():
    person[key] = basic_data[key]

for key in advanced_data:
    person[key] = advanced_data[key]

for key,value in person.items():
    print(f'{key}:{value}')