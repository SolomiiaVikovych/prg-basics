arr = [ -15, 8, -31, 47, -2, 19]



def max_value(n):
    maximum = 0
    for i in n:
        if i > maximum:
            maximum = i
    return maximum

def min_value(n):
    minimum = 0
    for i in n:
        if i < minimum:
            minimum = i
    return minimum

print(f'maximum value is {max_value(arr)}')

print(f'minimum value is {min_value(arr)}')

