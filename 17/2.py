import re

consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
vowels = {'a', 'e', 'i', 'o', 'u'}

strUser = input('Введите текст: ')
arr = strUser.split(' ')
strArr = ''
result = ''
resultUser = ''
pattern = r"[.,!?;:]"

for i in range(len(arr)):
    strArr = arr[i]
    if strArr[0].lower() in consonants:
        for j in range(len(strArr)):
            if strArr[j].lower() in vowels:
                result = strArr[j:].lower() + strArr[0:j].lower() + 'ау'
                result = re.sub(pattern, '', result)
                if strArr[len(strArr) - 1] in pattern:
                    result += strArr[len(strArr)-1] + ' '
                else:
                    result += ' '
                break

    elif strArr[0].lower() in vowels:
        result = strArr.lower() + 'way'
        result = re.sub(pattern, '', result)
        if strArr[len(strArr) - 1] in pattern:
            result += strArr[len(strArr)-1] + ' '
        else:
            result += ' '

    else:
        print('Error')
    if strArr[0] == strArr[0].upper():
        resultUser += result.title()
    else:
        resultUser += result

print(resultUser)
