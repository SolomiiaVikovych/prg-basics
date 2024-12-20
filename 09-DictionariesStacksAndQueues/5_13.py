def f(n):
    stack =[]
    char = n.split()
    for i in char:
        if i.isdigit():
            stack.append(i)
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(int(a)+int(b))
            elif i == '-':
                stack.append(int(a)-int(b))
            elif i == '*':
                stack.append(int(a)*int(b))
            elif i == '/':
                stack.append(int(a)/int(b))
    return stack[0]

print(f('2 3 +'))