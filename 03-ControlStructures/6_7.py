age = int(input('Enter your full age: '))
age_group = " "
if age >= 13 and age < 18:
    age_group = 'Teen'
elif age >= 18 and age <=64:
    age_group = 'Adult'
elif age >= 65:
    age_group = 'Senior'
print(f'Ypor age group is {age_group}')        