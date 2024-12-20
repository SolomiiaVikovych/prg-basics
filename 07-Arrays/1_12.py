categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max_expense = 0
count = 0
for i in expenses:
    if i > max_expense:
        max_expense = i
        count+=1

most_expensive = categories[count]
print(most_expensive)
