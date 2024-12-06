import re
patern = r'^[^\.]+\.[a-zA-Z0-9]{4}$'

with open('files.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if re.match(patern,line):
        print(line)

