arr =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)  


for row in arr:
    print(' '.join(map(str, row)))  # Print each row as a string of numbers