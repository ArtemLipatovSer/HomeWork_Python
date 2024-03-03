number = input("Введите целое число: ")

for i in number:
    if i == '3' or i == '6':
        number = number.replace(i, '')

print(number)
