EAN = input('Enter EAN code: ')

if len(EAN) == 12:
    correct = True
else:
    print('Incorrect number of characters')
    correct = False 
if correct:
    if EAN[0:3] == '590':
        made_in_poland = True
    else:
        made_in_poland = False

    if made_in_poland:
        print('The product was made in Poland')
    else:
        print('The product was not made in Poland')
