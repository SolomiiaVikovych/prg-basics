
import keyboard_input as keyboard # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('enter last name ')
age = keyboard.input_integer('enter age')
salary = keyboard.input_real('enter salary')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name: ', last_name)
print('Age: ', age)
if is_salary_hidden:
    print('Salary', salary)