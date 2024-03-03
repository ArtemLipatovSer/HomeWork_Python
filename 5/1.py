numOne = int(input('Введите начало диапазона: '))
numTwo = int(input('Введите конец диапазона: '))
sumEven = 0
averageEven = 0
countEven = 0
sumNotEven = 0
countNotEven = 0
sumNine = 0
count = 0
for i in range(numOne, numTwo, 1):
    print(i)
    if i % 2 == 0:
        sumEven = sumEven + i
        countEven += 1
    if i % 2 != 0:
        sumNotEven += i
        countNotEven += 1
    if i % 9 == 0:
        sumNine += i
        count += 1

print(f'Сумма четных чисел - {sumEven}, среднеарифметическое четных чисел - {sumEven/countEven}\n'
      f'Сумма нечетных чисел - {sumNotEven}, среднеарифметическое нечетных чисел - {sumNotEven/countNotEven}\n'
      f'Сумма чисел кратных 9 - {sumNine}, среднеарифметическое чисел кратных 9 - {sumNine/count}')


