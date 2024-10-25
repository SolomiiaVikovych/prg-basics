
def sum_digits(number):
    sum = 0 
    if number < 0:
        number = abs(number)
    number_str = str(number)
    for digit in number_str:
        ndigit = int(digit)
        sum +=  ndigit
    return sum    


    
any_number = int(input('Enter your number '))
result = sum_digits(any_number)
print(result)