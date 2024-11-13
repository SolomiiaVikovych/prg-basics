def fibonaci(n):
    a = 0
    b = 1
    n_fibonaci = [0,1]
    for i in range (n-2):
        next_num = a+b
        n_fibonaci.append(next_num)
        a = b
        b = next_num
    return n_fibonaci 

