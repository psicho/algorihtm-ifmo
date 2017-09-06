# Задача «Сортировка вставками»

with open("input.txt") as file:
    line = file.readlines(1)
    k = int(line[0])
    sort = list()
    line = file.readlines(2)[0].replace(' ','')
    sort = list(line)
    sdvig = dict()
    # print(sort)
    for i in range(1,k):
        j = i - 1
        n = i
        s = 0
        dig = sort[i]
        pos = i
        sdvig[dig] = pos + 1
        while j >= 0:
            if int(sort[n]) < int(sort[j]):
                temp = sort[j]
                sort[j] = sort[n]
                sort[n] = temp
                # print(sort)
                sdvig[dig] = j
                sdvig[sort[n]] = n
                # sdvig[dig] = j
                j = j - 1
                n = n - 1
                s = s + 1
                continue
            else: break
            # print(sort)
        if s > 0:
            sdvig[dig] = j + 2
    print(sdvig)
    print(sort)
            # sort = sort + line[i] + ' '


    # for line in file.readlines():
    #     line = line.split(' ')
    #     line = int(line[0]) + int(line[1])*int(line[1])


with open('output.txt', 'w') as file:
    file.write(str(sort))
