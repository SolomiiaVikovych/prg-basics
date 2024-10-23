old_price = float(input('Enter previous price: '))
new_price = float(input('Enter new price: '))
if new_price <= old_price*0.9:
    print('Buy the product!!! the price decreased by', (old_price - new_price)*100/old_price, "%")
else: 
    print("do not buy it, price did not decreased enough")    