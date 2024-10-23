decimal_number = int(input("Enter decimal number: "))
remainders = []
original_decimal = decimal_number
while decimal_number > 0:
    remainder = decimal_number % 2  
    remainders.append(remainder)     
    decimal_number //= 2              
binary_number = ''.join(str(bit) for bit in reversed(remainders))
print(f"{original_decimal}(10) = {binary_number}(2)")
