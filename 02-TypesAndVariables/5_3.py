a = input('a=')
b = input('b=')
c = input('c=')
a_int = int(a)
b_int = int(b)
c_int = int(c)
v= a_int*b_int*c_int
s = 2*(a_int*b_int+a_int*c_int+b_int*c_int)
print(f'volume={v} and surface area={s}')
