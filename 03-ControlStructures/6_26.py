password = '0805'
correct = False
for i in range(3):

    enter_password = input('Enter pasword: ')
    if enter_password == password:
      correct = True
    if correct:
        print("Correct password")
        break
    else:
        print('Try again')
if correct== False:
    print("Sorry your payment card is blocked ")