arr = [3, 2, 5, 3, 6, 2, 1]
unique = []
for i in set(arr):
    if arr.count(i) == 1:
        unique.append(i)

print(' '.join(map(str, unique)))