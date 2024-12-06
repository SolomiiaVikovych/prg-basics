with open('text.txt', 'w') as file:
        for i in range(1,101):
            squ = i**2
            cube = i**3
            line = f"{i},{squ},{cube},\n"
            file.write(line)
            



