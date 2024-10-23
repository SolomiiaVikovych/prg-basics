dogs_age = int(input('Enter dogs age: '))
in_human = 0
if dogs_age <=2:
    in_human = dogs_age*10.5
else:
    in_human = 4*(dogs_age - 2) + 21
print(f'Dogs age in human years = {in_human}')        