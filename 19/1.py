import random

arr = [random.randint(-11, 10) for i in range(21)]
average = int(sum(arr) / len(arr))
strNum = []
print(arr)  # Первоначальный массив

if average > 0:
    third = int((len(arr) / 3) * 2)

    for i in range(third):
        for j in range(0, third - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for i in range(third, len(arr)):
        strNum.append(arr[i])
    strNum.reverse()

    for i in range(len(strNum)):
        arr[i + third] = strNum[i]

else:
    third = int(len(arr) / 3)

    for i in range(third):
        for j in range(0, third - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for i in range(third, len(arr)):
        strNum.append(arr[i])
    strNum.reverse()

    for i in range(len(strNum)):
        arr[i + third] = strNum[i]

print(average)  # Среднеарифметическое суммы чисел массива
print(arr)  # Измененный массив
