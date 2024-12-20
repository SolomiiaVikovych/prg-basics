def one_d(m):
    onedm=[]
    for i in m:
        for j in i:
            onedm.append(j)
    return onedm
def print_array(m):
    return ' '.join(map(str,m))
arr = [[5,0,3,7,5], [9,0,9,1,2]]

print(print_array(one_d(arr)))