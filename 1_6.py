
avg_speed  = lambda km,h,m : km/(h+m/60)
distance = int(input('enter distance: '))
time_hours = float(input('enter time in hours: '))
time_minutes = float(input('enter time  minutes: '))
print(f'distance: {distance}')
print(f'time hours: {time_hours}')
print(f'time minutes: {time_minutes}')
print(f'average speed: {avg_speed(distance,time_hours,time_minutes)}')