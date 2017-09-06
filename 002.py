# Задача «a+b^2»

with open("input.txt") as file:

    for line in file.readlines():
        line = line.split(' ')
        line = int(line[0]) + int(line[1])*int(line[1])

    with open('output.txt', 'w') as file:
        file.write(str(line))

