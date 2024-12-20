# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
food = monthly_expenses[0][0]+ monthly_expenses[1][0] + monthly_expenses[2][0]
transport = monthly_expenses[0][1]+ monthly_expenses[1][1] + monthly_expenses[2][1]
utilities = monthly_expenses[0][2]+ monthly_expenses[1][2] + monthly_expenses[2][2]

def weekly_expenses(week):
    sum = 0
    expenses = monthly_expenses[week-1]
   
    for i in expenses:
        sum += i
    return sum
total = 0
for i in monthly_expenses:
    for j in i:
        total+= j


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', weekly_expenses(1))
print('Week 2:', weekly_expenses(2))
print('Week 3:', weekly_expenses(3))
print('Week 4:', weekly_expenses(4))
print('---------------')
print('TOTAL:', total)