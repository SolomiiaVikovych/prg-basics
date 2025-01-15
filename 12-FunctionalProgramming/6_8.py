grades = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit
limit1 = 70
limit2 = 40
limit3 = 30

print(
   f' Min 70 pts: {list(filter(min_pts(limit1),grades))}\n'
   f'Min 40 pts: {list(filter(min_pts(limit2),grades))}\n'
   f' Min 30 pts: {list(filter(min_pts(limit3),grades))}'
)


