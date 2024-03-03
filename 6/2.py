count = 0
for i in range(100, 1000):
    i1 = int(i / 100)
    i2 = int(i % 10)
    i3 = int((i % 100) / 10)
    if i1 == i2 or i2 == i3 or i3 == i1:
        count += 1
print(f'Количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры - {count}')

