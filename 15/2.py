oneWord = input('Введите первое слово: ')
twoWord = input('Введите второе слово: ')

if oneWord == twoWord[::-1]:
    print('Это анаграмма')
else:
    print('Слова обычные')


