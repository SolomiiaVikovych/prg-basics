user_str = input('enter ane text: ')

def f(str):
 stack = []
 for i in str:
    stack.append(i)
 reversed_str = ''
 for i in range(len(str)):
    reversed_str += stack.pop()
 return reversed_str
 
print(f(user_str))
