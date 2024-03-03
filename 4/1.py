number = int(input('Введите число в диапазоне от 1 до 100: '))

if 100 >= number >= 1:
    if number % 3 == 0:
        if number % 5 == 0:
            print('Fizz Buzz')
        else:
            print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
else:
    print('Ввели неправильный диапазон')
