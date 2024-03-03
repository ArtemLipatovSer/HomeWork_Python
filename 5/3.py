while True:
    number = int(input("Введите число: "))
    if number == 7:
        print('Good bye!')
        break
    if number > 0:
        print('Number is positive')
    if number < 0:
        print('Number is negative')
    if number == 0:
        print('Number is equal to zero')
