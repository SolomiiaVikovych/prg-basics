number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number2: ')) 
operator = input('Enter operator ')

if operator == "*":
    result = number1 * number2
elif operator == "+":
    result = number1 = number2
elif operator == "-":
    result = number1 - number2
elif operator=="/":
    result = number1 / number2

# print result
print(f'{number1} {operator} {number2} = {result}')