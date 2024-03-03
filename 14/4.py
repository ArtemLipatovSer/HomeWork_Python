book = {
    'автор': 'Харбанс Ришал',
    'название книги': 'Грокаем алгоритмы',
    'жанр': 'Зарубежная компьютерная литература',
    'год выпуска': 2017,
    'количество страниц': 288,
    'издательство': 'Питер'
}


# Добавление
def addInfo(arr):
    newInfo = {input('Какую информацию хотите добавить: \n').lower(): input('Введите информацию: \n').lower()}
    arr.update(newInfo)


# Удаление
def delInfo(arr):
    arr.pop(input('Введите информацию, которую хотите удалить:\n').lower(), 'Такого нет')


# Поиск
def findInfo(arr, key):
    print(arr.get(key, "Такого нет"))


# Изменение данных
def changeInfo(arr, data):
    arr.update(data)


if __name__ == '__main__':
    check = int(input('Что будем делать?\n\t'
                      '1. Добавить информацию\n\t'
                      '2. Удалить информацию\n\t'
                      '3. Найти информацию\n\t'
                      '4. Изменить информацию\n'))
    if check == 1:
        addInfo(book)
    elif check == 2:
        delInfo(book)
    elif check == 3:
        info = input('Какую информацию нужно найти: ')
        findInfo(book, info)
    elif check == 4:
        newInfo = {input('Какую информацию вы хотите изменить: '): input('Что вы хотите изменить: ')}
        changeInfo(book, newInfo)
    else:
        print('Error')

print(book)
