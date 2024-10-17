# Height in centimeters
cm = 170

# Conversion factors
cm_per_foot = 30.48
cm_per_inch = 2.54

# Calculate the number of feet
feet = cm // cm_per_foot  # Integer division to get the whole number of feet

# Calculate the remaining inches
inches = (cm % cm_per_foot) / cm_per_inch  # Modulus to get remaining cm and convert to inches

# Print the result
print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {inches:.2f} inches.')
