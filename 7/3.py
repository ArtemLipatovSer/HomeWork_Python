startNum = int(input('Введите начало: '))
endNum = int(input('Введите конец: '))
for i in range(startNum, endNum+1):
    print('\n')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j};', end=' ')
