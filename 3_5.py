arr = [15, 8, 31, 47, 2, 19]

def arithmetic_mean(n):
    sum  = 0
    for i in n:
        sum += i

    return sum/len(n)

print('array: ', ' '.join(map(str, arr)))
print('arithmetic mean of array elemnts ', arithmetic_mean(arr) )