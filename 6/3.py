count = 0
ind = 0
for i in range(100, 10000):
    i1 = int(i / 1000)
    i2 = int((i / 100) % 10)
    i3 = int((i % 100) / 10)
    i4 = int(i % 10)
    if i1 != i2 and i1 != i3 and i1 != i4 and i2 != i3 and i2 != i4 and i3 != i4:
        count += 1
print(f'Количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры - {count}')





