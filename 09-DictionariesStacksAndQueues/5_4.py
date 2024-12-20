winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

total = 0
for hour in winter_semester.values():
    total+= hour

print(f'total hours spent i nwinter semester: {total}')