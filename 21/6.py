from os import strerror
import re

wordOne = input('Введите слово которое хотите заменить: \n')
wordTwo = input('Введите слово на какое хотите заменить: \n')

try:
    with open('files/text6.txt', 'r') as file:
        line = file.readlines()
        j = 0
        lineArr = []
        while j != len(line):
            arr = line[j].split()
            for i in range(len(arr)):
                arr[i] = re.sub(r'[^\w\s]', '', arr[i])
                if arr[i] == wordOne:
                    arr[i] = wordTwo
            lineArr.append(arr)
            j += 1

    with open('files/text7.txt', 'w') as file:
        strLine = ''
        for i in lineArr:
            a = ' '.join(i)
            strLine += a + '.' + '\n'
        file.write(strLine)


except IOError as e:
    print(strerror(e.errno))
