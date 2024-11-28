# Original array
array = [15, 8, 31, 47, 2, 19]

# Printing the existing array
print("Existed array:", " ".join(map(str, array)))

# Reversing the array using a loop
reverse_array = []
for i in range(len(array) - 1, -1, -1):
    reverse_array.append(array[i])

# Printing the reversed array
print("Reverse array:", " ".join(map(str, reverse_array)))
 