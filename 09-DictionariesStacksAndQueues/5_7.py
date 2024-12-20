hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
        hotel_names = [hotel["name"] for hotel in hotels]
        return ','.join(hotel_names)
    
def avg_price(hotels):
    sum = 0 
    count = 0
    for i in hotels:
        sum += i["price"]
        count += 1
    return f'{(sum/count):.0f}'
if avg_price(hotels_in_Sopot) < avg_price(hotels_in_Krakow):
    cheaper = 'Sopot'
elif avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    cheaper = 'Krakow'
else:
    cheaper = 'same for both'

print( f' Hotels in Krakow: {hotel_list(hotels_in_Krakow)}')
print(f' avarage price for hotels n krakow {avg_price(hotels_in_Krakow)}')
print(f' Hotels in Sopot: {hotel_list(hotels_in_Sopot)}')
print(f' average price for hotels in Sopot: {avg_price(hotels_in_Sopot)}')
print(f'cheaper average price in : {cheaper}')