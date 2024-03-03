strUser = input('Введите текст: ')
strWord = input('Введите слова: ')
strUser = strUser.lower()
strUser = strUser.split()
strWord = strWord.lower()
strWord = strWord.split()
print(strUser)
print(strWord)
for i in range(len(strUser)):
    for j in strWord:
        if strUser[i] == j:
            strUser[i] = strUser[i].capitalize()

print(strUser)
