arr = [7,9,2,4,5,6]
evens = [num for num in arr if num%2 == 0]
odds = [num for num in arr if num%2 != 0]
print(f'oraginal array {arr}')
print(f'sorted array {evens+odds}')