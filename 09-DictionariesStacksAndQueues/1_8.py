price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print('Prices before discount')
for key,value in price_list.items():
    print(f'{key}:{value}')
total_pre_discount = 0
for value in price_list.values():
    total_pre_discount+=value

print(f'total value of items before discount: {total_pre_discount:.2f}')

for product,price in price_list.items():
    price_list[product] = price*0.9

total = 0
for value in price_list.values():
    total+= value
print(f'total value after discount : {total:.2f}')
