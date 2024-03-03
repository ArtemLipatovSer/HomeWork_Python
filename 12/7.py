def palindrome(num):
    arrOne = []
    arrTwo = []
    if len(str(num)) % 2 == 0:
        for i in range(int(len(str(num))/2)):
            arrOne.append(str(num)[i])
        for i in range(int(len(str(num))/2), len(str(num))):
            arrTwo.insert(0, (str(num)[i]))
        print(arrOne)
        print(arrTwo)
    else:
        return 'error'
    if arrOne == arrTwo:
        return 'Число палиндром'
    else:
        return 'Число не палиндром'


print(palindrome(11))


