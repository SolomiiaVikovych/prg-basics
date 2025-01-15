bottles =[508,500,512,499,492,511,503,476,501,509]
filled_correctly = list(filter(lambda x: 500*0.98<= x  <= 500*1.02,bottles))

percentage = (len(bottles)-len(filled_correctly))/len(bottles)*100

print(
    f'Bottle capacity: 500ml\n'
    f'tolerance: 2%\n'
    f'bottles filled: {','.join(map(str,bottles))}\n '
    f'Incorrectly filled:{percentage}%'
    
)