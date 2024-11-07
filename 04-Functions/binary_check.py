def binary(number):
    user_n = input('enter number in binary ')
    for i in user_n:
        if i == '1' or i == '0':
         is_binary = True
        else:
           is_binary = False
           break
    if is_binary == True:
        return True
    else:
        return False    