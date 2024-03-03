consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
vowels = {'a', 'e', 'i', 'o', 'u'}

strUser = input('Введите текст: ')
arr = strUser.split(' ')
strArr = ''
result = ''
resultUser = ''

for i in range(len(arr)):
    strArr = arr[i]
    if strArr[0].lower() in consonants:
        for j in range(len(strArr)):
            if strArr[j].lower() in vowels:
                result = strArr[j:].lower() + strArr[0:j].lower() + 'ау' + ' '
                break
    elif strArr[0].lower() in vowels:
        result = strArr.lower() + 'way' + ' '
    else:
        print('Error')
    resultUser += result

print(resultUser)
