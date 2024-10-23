###
# Program that simulates the operation of an electronic thermometer.
#
temperature = float(input('Enter temperature in degrees Celsius'))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It's hot")
elif temperature >= 15:
    print("it's warm")
elif temperature >=0:
    print("It's cold")
elif temperature < 0:
    print("Warning. Frost")    