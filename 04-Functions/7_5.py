import range
a = int(input('enter number '))

number_check = range.chech_if_in_range(a)
if number_check:
    print(f'number {a} is in range ' )
else:
    print(f'number {a} ia not in range ')

