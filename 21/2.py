from os import strerror

try:
    nStr = nSmb = nNum = nVow = nCons = 0
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    fileOne = open('files/text1.txt', 'rt')
    fileTwo = open('files/textInfo.txt', 'wt')
    lines = fileOne.readlines()

    for line in lines:
        nStr += 1
        for ch in line:
            nSmb += 1
            if ch in consonants:
                nCons += 1
            if ch in vowels:
                nVow += 1
            if ch in str(nNum):
                nNum += 1
    fileTwo.write(f'Количество строк = {nStr}\n'
                  f'Количество символов = {nSmb}\n'
                  f'Количество гласных букв = {nVow}\n'
                  f'Количество согласных букв = {nCons}\n'
                  f'Количество цифр = {nNum}')
except IOError as e:
    print(strerror(e.errno))
