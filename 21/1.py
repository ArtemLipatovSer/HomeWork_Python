from os import strerror

try:
    fileOne = open('files/text1.txt', 'rt')
    fileTwo = open('files/text2.txt', 'rt')
    readOne = fileOne.readlines()
    readTwo = fileTwo.readlines()
    for i in range(len(readOne)):
        if readOne[i] != readTwo[i]:
            print(f'Несовпадающая строка №{i} первого файла - {readOne[i]}'
                  f'Несовпадающая строка №{i} второго файла - {readTwo[i]}')
    fileOne.close()
    fileTwo.close()
except IOError as e:
    print(strerror(e.errno))
