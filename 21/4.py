from os import strerror

try:
    with open('files/text4.txt', 'r') as file:
        lines = file.readlines()
        size = 0
        strFile = ''
        for line in lines:
            if len(line) > size:
                size = len(line)
                strFile = line
    print(f'Самая длинная строка - {strFile}Длиной - {size} символов')
except IOError as e:
    print(strerror(e.errno))
