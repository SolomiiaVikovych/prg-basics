def chech_if_in_range(n):
    user_n = int(input('enter number '))
    user_range_x = int(input('enter minimum of range '))
    user_range_y = int(input('enter maximum of your range '))
    if user_n >= user_range_x and user_n <= user_range_y:
        return True
    else:
        return False