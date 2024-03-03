import random

nameBook = ['Книга №5', 'Книга №3', 'Книга №2', 'Книга №4', 'Книга №1']
yearOfPub = [random.randint(1990, 2023) for i in range(5)]

arrBooks = []
for i in range(len(nameBook)):
    arr = [nameBook[i], yearOfPub[i]]
    arrBooks.append(arr)
print(arrBooks)


def sortName(arr):
    return sorted(arr)


def sortYear(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[minimum][1]:
                minimum = j
        arr[minimum][0], arr[i][0], arr[minimum][1], arr[i][1] = arr[i][0], arr[minimum][0], arr[i][1], arr[minimum][1]
    return arr


def printBooks(arr):
    for i in range(len(arr)):
        strPhoneNumber = ''
        strBooks = ''.join(str(arr[i]))
        print(strBooks)


if __name__ == '__main__':

    while True:
        check = int(input('Выберете действие:\n'
                          '1. Отсортировать по названию книги\n'
                          '2. Отсортировать по дате публикации книги\n'
                          '3. Вывести список книг\n'
                          '4. Выход\n'))
        if check == 1:
            print(sortName(arrBooks))
        elif check == 2:
            print(sortYear(arrBooks))
        elif check == 3:
            printBooks(arrBooks)
        elif check == 4:
            break
        else:
            print('Неправильное действие!')
