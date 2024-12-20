def comparison (arr1, arr2):
    if arr1 == arr2:
        return True
    else:
        return False 
            
arr_1 = [True,False]
arr_2 = [True,False,True]
if comparison(arr_1, arr_2) == True:
    comp = 'arrays are the same'
else:
    comp = 'arrays are diffirent'

print('array 1 ', ' '.join(map(str, arr_1)))
print('array 2 ', ' '.join(map(str, arr_2)))
print('Comparison: ', comp)

 