basic_salary = 5000
total_salary = 0
bonus_check = input('Do you have a bonus? (Y/N)')
if bonus_check == "Y":
    is_bonus = True
else:
    is_bonus = False
if is_bonus == True:
    bonus = int(input('Entrer percentage of a bonus: '))
    total_salary = basic_salary*bonus/100 + basic_salary
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')  