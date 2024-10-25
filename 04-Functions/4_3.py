import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    result = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
    return result
area345= triangle_area(3,4,5)
area51213= triangle_area(5,12,13)
area72425= triangle_area(7,24,25)



print('The area of ​​a triangle with sides 3,4 ,5  is ',area345 )
print('The area of ​​a triangle with sides 5,12,13 is ', area51213)
print('The area of ​​a triangle with sides 7,24,25 is ', area72425)