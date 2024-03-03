men = {
    'ФИО': 'Иванов А.С.',
    'телефон': '911-911',
    'email': '123@mail.ru',
    'должность': 'инженер',
    'номер кабинета': 123,
    'skype': '123'
}


# Добавление
def addInfo(arr):
    newInfo = {input('Какую информацию хотите добавить: \n'): input('Введите значение: \n').lower()}
    arr.update(newInfo)


# Удаление
def delInfo(arr):
    arr.pop(input('Введите информацию, которую хотите удалить:\n'), 'Такого нет')


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
        addInfo(men)
    elif check == 2:
        delInfo(men)
    elif check == 3:
        info = input('Какую информацию нужно найти: ')
        findInfo(men, info)
    elif check == 4:
        newInfo = {input('Какую информацию вы хотите изменить: '): input('Что вы хотите изменить: ')}
        changeInfo(men, newInfo)
    else:
        print('Error')

print(men)
