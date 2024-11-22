def binary(user_n):
    
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