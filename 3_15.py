# Define the tuple
original_tuple = (10, 20, 30, 40, 50)

# Reverse the tuple
reversed_tuple = original_tuple[::-1]

# Print the results
print("Tuple:", ",".join(map(str, original_tuple)))
print("Reverse order:", ",".join(map(str, reversed_tuple)))