def f(n1,n2,n3):
    max_num = max(n1,n2,n3)
    min_num = min(n1,n2,n3)
    return max_num - min_num

number1 = int(input('enter first number '))
number2 = int(input('enter second number '))
number3 = int(input('enter third number '))
print(f(number1,number2,number3))