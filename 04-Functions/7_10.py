def f(x, y):
    count = 0
    for num in range(x, y + 1):
        if num < 0 and num % 2 == 0:
            count += 1
    return count