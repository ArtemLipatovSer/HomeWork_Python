numOne = int(input('Введите число х: '))
numTwo = int(input('Введите число y: '))
step = numOne
for i in range(numTwo-1):
    step *= numOne
print(step)
print(numOne**numTwo)
