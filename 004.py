# Задача «Знакомство с жителями Сортлэнда»

with open("input.txt") as file:
    line = file.readlines(1)
    k = int(line[0])
    sort = list()
    line = file.readlines(2)[0].split(' ')
    sort = line.copy()
    stru = ''
    stru = stru + '1' + ' '
    for i in range(1,k):
        j = i - 1
        n = i
        while j >= 0:
            if float(sort[n]) < float(sort[j]):
                temp = sort[j]
                sort[j] = sort[n]
                sort[n] = temp
                j = j - 1
                n = n - 1
                continue
            else:
                break
    p1 = line.index(sort[0])
    p2 = line.index(sort[len(sort)//2])
    p3 = line.index(sort[-1])
with open('output.txt', 'w') as file:
    file.write(str(p1+1) + ' ' + str(p2+1) + ' ' + str(p3+1))
