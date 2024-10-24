
amount = int(input("Enter the amount in PLN: "))

five_pln_coins = 0
two_pln_coins = 0
one_pln_coins = 0

if amount >= 5:
    five_pln_coins = amount // 5
    amount %= 5 
    two_pln_coins = amount // 2
    amount %= 2  
one_pln_coins = amount 

print(f"The amount of PLN {sum([five_pln_coins * 5, two_pln_coins * 2, one_pln_coins])} in coins:")
print(f"5 PLN coins: {five_pln_coins}")
print(f"2 PLN coins: {two_pln_coins}")
print(f"1 PLN coins: {one_pln_coins}")


