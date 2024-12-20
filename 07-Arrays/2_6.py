matrix =[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
count = 0
for i in matrix:
    i[count] = 1
    count+=1
for i in matrix:
    print(i)