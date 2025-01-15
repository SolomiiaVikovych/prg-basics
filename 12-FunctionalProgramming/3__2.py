sentence = 'I completely agree with you'
result = list(map(lambda x:len(x) , sentence.split()))
print(f'No. of leters in each word: {result}')