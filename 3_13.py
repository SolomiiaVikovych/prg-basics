def occurs(number, array):
    if number in array:
        return True
    else:
        return False

arr = [15, 38, 7, 23, 6, 5]

num = int(input(' enter number '))
if occurs(num, arr) == True:
   occ = ' is in array'
else:
    occ = 'is not in array'
   

print ('Array ', ' '.join(map(str, arr)))
print(f' number {num} {occ}')
