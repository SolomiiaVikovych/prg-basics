arr = [[1,3,4,2,6],[5,4,3,2,1],[6,7,8,9,0] ]
arr1 = reversed(arr)

   
for row in arr:
    print(' '.join(map(str,row)))

print()

for row in arr1:
    print(' '.join(map(str,row)))