def counter_add():
    def add(num):
        num += 5
        return num

    return add


k = int(input('Введите число: '))
cnt = counter_add()
result = cnt(k)
print(result)
