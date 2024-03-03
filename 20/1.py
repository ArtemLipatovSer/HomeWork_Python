import random

arrId = [random.randint(1, 100) for i in range(10)]
arrNumber = [random.randint(100000, 1000000) for i in range(10)]
print(arrId, arrNumber, sep='\n')

arrPhoneNum = []
for i in range(len(arrId)):
    arr = [arrId[i], arrNumber[i]]
    arrPhoneNum.append(arr)
print(arrPhoneNum)


def selection_sort_id(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j][0] < arr[minimum][0]:
                minimum = j
        arr[minimum][0], arr[i][0], arr[minimum][1], arr[i][1] = arr[i][0], arr[minimum][0], arr[i][1], arr[minimum][1]
    return arr


def selection_sort_num(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[minimum][1]:
                minimum = j
        arr[minimum][0], arr[i][0], arr[minimum][1], arr[i][1] = arr[i][0], arr[minimum][0], arr[i][1], arr[minimum][1]
    return arr


def printPhoneNumber(arr):
    for i in range(len(arr)):
        strPhoneNumber = ''
        strPhoneNumber = ''.join(str(arr[i]))
        print(strPhoneNumber)


if __name__ == '__main__':

    while True:
        check = int(input('Выберете действие:\n'
                          '1. Отсортировать по идентификационным кодам\n'
                          '2. Отсортировать по номерам телефона\n'
                          '3. Вывести список телефонов\n'
                          '4. Выход\n'))
        if check == 1:
            print(selection_sort_id(arrPhoneNum))
        elif check == 2:
            print(selection_sort_num(arrPhoneNum))
        elif check == 3:
            printPhoneNumber(arrPhoneNum)
        elif check == 4:
            break
        else:
            print('Неправильное действие!')
