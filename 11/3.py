def simpleNum(list):
    count = 0
    simpleCount = 0
    for i in range(0, len(list)):
        for j in range(2, list[i]):
            if list[i] % j == 0:
                count += 1
        if count <= 0:
            simpleCount += 1
    return simpleCount


arr = [2, 3, 5, 7, 11, 13, 4, 6]

print(f'Количество простых чисел в списке - {simpleNum(arr)}')
