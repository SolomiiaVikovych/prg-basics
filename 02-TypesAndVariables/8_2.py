def celsius_to_kelvin(celsius):
    return celsius + 273.15
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input('Enter temperature in Celsius: '))
kelvin = celsius_to_kelvin(celsius)
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'Temperature in Kelvin: {kelvin}')
print(f'Temperature in Fahrenheit: {fahrenheit}')