def arithmetic(n1,n2,operator):
    if operator == '+':
      result = n1 + n2
    elif operator == '-':
       result = n1 - n2
    elif operator == '*':
       result = n1 * n2
    elif operator == '/':
       result = n1/n2
    elif operator == '%':
       result = n1%n2
    elif operator == '**':
       result = n1**n2


    return result

num1 = int(input('enter number 1 '))
num2 = int(input('enter number 2 '))
user_operator = input('enter operato (+,-,*,/,%,**) ') 
print(f' {num1} {user_operator} {num2} = {arithmetic(num1,num2,user_operator)}')        
     

