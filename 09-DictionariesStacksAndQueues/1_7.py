a ={
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total = 0
for num in a.values():
    total+= num


for key,value in a.items():
    print(f'{key}: {value}')

print('total number of items in store: ', total) 