arr = [2, -7, 4, 15,244,42,48,1,3,7]
num = float(input('enter number'))
c = 0
for i in arr:
    if i > num:
        c+=1

print(f'there are {c} number that are grater then {num}')