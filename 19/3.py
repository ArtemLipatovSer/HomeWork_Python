import random

arr = [random.randint(1, 20) for i in range(20)]
print(arr)


def sortArr(arr):
    sortGrade = True
    while sortGrade:
        sortGrade = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sortGrade = 1
    return arr


print(sortArr(arr))
