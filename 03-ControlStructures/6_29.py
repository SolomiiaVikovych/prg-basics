# Input: Number of leading prime numbers to find
N = int(input("Enter the number of leading prime numbers to find: "))

# Initialize variables
count = 0  # To count how many primes have been found
num = 2    # Start checking from the first prime number

# Loop to find N prime numbers
while count < N:
    # Check if the current number is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # If prime, print it and increment the prime count
    if is_prime:
        print(num, end=' ')
        count += 1
    
    # Check the next number
    num += 1

print()  # New line after printing all prime numbers
