import csv
try:
    with open('clothing.csv', 'r')as file:
        reader = csv.DictReader(file)

        for row in reader:
           name = row.get('Product_Name')
           pr_id = row.get('Product_ID')
           category = row.get('Category')
           color = row.get('Color')
           size = row.get('Size')
           price = row.get('Price')
           stock = row.get('Stock_Quantity')
           if float(price) < 60 and float(stock) < 40:
               print(name, pr_id, category, color, size)
               
except FileNotFoundError:
    print('file doesnt exist')
