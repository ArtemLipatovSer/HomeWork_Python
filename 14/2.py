words = {'hello': 'привет', 'bye': 'пока', 'program': 'программа'}


# Добавление
def addWord(arr):
    newWord = {input('Введите слово на английском: \n').lower(): input('Введите перевод на русский: \n').lower()}
    arr.update(newWord)


# Удаление
def delWord(arr):
    arr.pop(input('Введите слово, которое хотите удалить:\n').lower(), 'Такого слова нет')


# Поиск
def findWords(arr, key):
    print(arr.get(key, "Такого нет"))


# Изменение данных
def changeWord(arr, data):
    arr.update(data)


if __name__ == '__main__':
    check = int(input('Что будем делать?\n\t'
                      '1. Добавить слово\n\t'
                      '2. Удалить слово\n\t'
                      '3. Перевод слова\n\t'
                      '4. Изменить слово\n'))
    if check == 1:
        addWord(words)
    elif check == 2:
        delWord(words)
    elif check == 3:
        word = input('Какое слово нужно перевести: ').lower()
        findWords(words, word)
    elif check == 4:
        newWords = {input('Какое слово вы хотите изменить: ').lower(): input('Что вы хотите изменить: ').lower()}
        changeWord(words, newWords)
    else:
        print('Error')

print(words)
