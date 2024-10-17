import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("enter your guess: "))
victory =(computer==you)
print(f'You won: {victory}')