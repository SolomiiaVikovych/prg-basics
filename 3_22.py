import random

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]

arr = [2,3,6,1,9,5]
print(rand_elem(arr))