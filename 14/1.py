players = {'K.Bryant': 198, 'M.Jordan': 198, 'J.Williams': 185}

# Добавление
def addPlayers(arr):
    newPlayer = {'J.Lebron': 206}
    arr.update(newPlayer)

# Удаление
def delPlayers(arr):
    arr.pop('J.Williams', 'Такого нет')

# Поиск
def findPlayers(arr, key):
    print(arr.get(key, "Такого нет"))

# Изменение данных
def changePlayers(arr, data):
    arr.update(data)


if __name__ == '__main__':
    check = int(input('Что будем делать?\n\t'
                      '1. Добавить баскетболиста\n\t'
                      '2. Удалить баскетболиста\n\t'
                      '3. Найти данные баскетболиста\n\t'
                      '4. Изменить данные баскетболиста\n'))
    if check == 1:
        addPlayers(players)
    elif check == 2:
        delPlayers(players)
    elif check == 3:
        player = 'M.Jordan'
        findPlayers(players, player)
    elif check == 4:
        newPlayer = {'K.Bryant': 199}
        changePlayers(players, newPlayer)
    else:
        print('Error')

print(players)



