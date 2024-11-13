def check(password):
    c = 0
    if_repeats = False
    is_6 = True
    for i in set(password):
        m = password.count(i)
        if m > 1:
            if_repeats = True
    if len(password) < 6:
        is_6 = False
    if is_6 == True and if_repeats == False:
        return True
    else:
        return False
    

user_password = input('enter pasword ')
print(check(user_password))    
