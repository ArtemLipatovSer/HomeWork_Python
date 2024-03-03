import math

# Программа

def inputGrade(arr):
    print(f'Вывод оценок: {arr}')


def retake(arr):  # Пересдача
    elem = int(input('Введите номер элемента: '))
    grade = int(input('Введите новую оценку: '))
    arr[elem - 1] = grade
    return arr


def scholarship(arr):
    result = sum(arr) / len(arr)
    if result < 10.7:
        print('Стипендии нет')
    else:
        print('Стипендия есть')


def sortArr(arr):
    sortGrade = True
    while sortGrade:
        sortGrade = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sortGrade = True
    return arr


if __name__ == '__main__':
    index = 0
    arr = []
    while index < 5:
        index += 1
        grade = int(input(f"Введите оценку №{index} (от 1 до 12): "))
        arr.append(grade)

    check = int(input('Выберите действие:\n'
                      '1. Вывод оценок\n'
                      '2. Пересдача экзамена\n'
                      '3. Выходит ли стипендия\n'
                      '4. Отсортировать список оценок по возрастанию\n'))
    match check:
        case 1:
            inputGrade(arr)
        case 2:
            print(retake(arr))
        case 3:
            scholarship(arr)
        case 4:
            print(sortArr(arr))
