stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
price = lambda x: x[0]*x[1]
prices = list(map(price,stock))
print(sum(prices))