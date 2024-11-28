def subset(arr1,arr2):
    count = 0
    for i in arr1:
        if i in arr2:
            count+=1
    if count == len(arr1):
        return True
    else:
        return False
    
ar2 = [2, 3, 4, 5, 6, 7, 8, 9, 0]
ar1 = [3, 5, 7]

print(subset(ar1,ar2))