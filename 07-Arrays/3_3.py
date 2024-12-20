arr = [8, 5, 2, 1, 9]
for i in range(len(arr)):
    arr[i] = arr[i]**2
     

print(' '.join(map(str, arr)))