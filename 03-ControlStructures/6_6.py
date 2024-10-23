hours_parked = float(input('Enter for how long the car has been parked in hours: '))
parking_fee = 0
if hours_parked >= 1 and hours_parked <= 2:
    parking_fee = 5
elif hours_parked >= 3 and hours_parked <= 6:
    parking_fee = 15
elif hours_parked > 6:
    parking_fee = 20
elif hours_parked < 0 :
    print('Error : can not be less then 0')    
print(f'Parking fee is {parking_fee} PLN')