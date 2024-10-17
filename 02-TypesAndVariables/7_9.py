import random
dice = random.randint(1,6)
special_number = (dice== 1 or dice == 6)
print("dice: ", dice)
print(f'Special number: {special_number}')