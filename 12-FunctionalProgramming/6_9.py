# Dictionary of temperatures recorded in different towns
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Filter towns with positive temperatures using an anonymous function
positive_temps = filter(lambda town: temperatures[town] > 0, temperatures)

# Convert the result to a list and join town names with a space
result = " ".join(positive_temps)

# Display the result
print("Cities with positive temperatures:", result)

 


