# Задача «Сортировка вставками»

with open("input.txt") as file:
    line = file.readlines(1)
    k = int(line[0])
    sort = list()
    line = file.readlines(2)[0].split(' ')
    sort = line
    # print(sort)
    sdvig = dict()
    stru = ''

    stru = stru + '1' + ' '

    for i in range(1,k):
        j = i - 1
        n = i
        s = 0
        while j >= 0:
            if int(sort[n]) < int(sort[j]):
                temp = sort[j]
                sort[j] = sort[n]
                sort[n] = temp
                j = j - 1
                n = n - 1
                s = s + 1
                continue
            else:
                break
        if i == 1:
            stru = stru + str(n+1) + ' '
        if s > 0 and i > 1:
            stru = stru + str(n+1) + ' '
        if i > 1 and s == 0:
            stru = stru + str(n+1) + ' '
    sort = str(sort).replace('[','').replace(']','').replace("'",'').replace(',','').strip()
    stru = stru.strip()

with open('output.txt', 'w') as file:
    file.write(stru + '\n' + sort)
