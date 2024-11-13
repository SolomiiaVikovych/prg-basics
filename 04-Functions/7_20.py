def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Only check divisors up to the square root
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0  # To count the primes we find
    num = 2    # Start checking from the first prime number
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1  # Move to the next number
