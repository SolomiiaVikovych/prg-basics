from functools import reduce
numbers = [2,4,6,3,7,5]
even = list(filter(lambda x: x%2 == 0, numbers))
add = lambda x,y: x+y
result = reduce(add,even)
print(result)