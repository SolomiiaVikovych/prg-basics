grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
non_negative = list(filter(lambda x: x>2,grades))
sum = 0
for i in range(len(non_negative)):
    sum += non_negative[i]

arit_mean = sum/len(non_negative)


print(f'Arithmetic mean for grades <> 2.0 is {round(arit_mean,2)}')

    