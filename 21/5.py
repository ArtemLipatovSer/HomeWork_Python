from os import strerror
import re

wordUser = input('Введите слово: \n')

try:
    with open('files/text4.txt', 'r') as file:
        line = file.readline()
        count = 0
        while line != '':
            line = re.sub(r'[^\w\s]', '', line)
            line = line.replace('\n', '')
            arr = line.split(' ')
            for i in arr:
                if wordUser == i.lower():
                    count += 1
            line = file.readline()
    print(f'Слово {wordUser} в тексте встречается {count} раз/раза')

except IOError as e:
    print(strerror(e.errno))
