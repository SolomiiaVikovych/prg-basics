def second_largest(arr):
    ordered_arr = sorted(arr)
    return ordered_arr[-2]

def min_max_diff(arr):
    return max(arr) - min(arr)


def median(numbers):
   return numbers[len(numbers)//2]
def mimax(arr):
    return [min(arr), max(arr)]
def str_minus(arr):
    return '-'.join(map(str, arr))