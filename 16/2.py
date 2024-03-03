import string


def dictAlphabet(arr, num, words):
    for i in range(len(arr)):
        if i >= (len(arr) - num):
            words.update({arr[i]: arr[(i + num) - len(arr)]})
        else:
            words.update({arr[i]: arr[i + num]})


def encrypt(str, arr):
    result = ''
    for i in range(len(str)):
        if str[i] == ' ':
            result += ' '
        for key, value in arr.items():
            if str[i].upper() == key:
                result += value
    return result


def decipher(str, arr):
    result = ''
    for i in range(len(str)):
        if str[i] == ' ':
            result += ' '
        for key, value in arr.items():
            if str[i].upper() == value:
                result += key
    return result


if __name__ == '__main__':
    alphabet = list(string.ascii_uppercase)
    dictWords = {}
    check = int(input('Выберете действие: \n'
                      '1. Зашифровать:\n'
                      '2. Расшифровать:\n'))
    if check == 1:
        strUser = input('Введите строку, которую хотите зашифровать: ')
        shift = int(input('Введите количество сдвигов в алфавите: '))
        dictAlphabet(alphabet, shift, dictWords)
        print(encrypt(strUser, dictWords))
    elif check == 2:
        strUser = input('Введите строку, которую хотите расшифровать: ')
        shift = int(input('Введите количество сдвигов в алфавите: '))
        dictAlphabet(alphabet, shift, dictWords)
        print(decipher(strUser, dictWords))
    else:
        print('Такого действия нет!')
