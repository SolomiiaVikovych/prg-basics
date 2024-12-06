import re
num = 0
text = input('enter text ')
patern = r'[aoueiy]'
for i in text:
    if re.match(patern,i):
        num+=1
print(num)
