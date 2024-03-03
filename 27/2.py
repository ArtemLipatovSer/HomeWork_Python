def counter_add(n):
    def increase(num):
        return num*n
    return increase

cnt = counter_add(2)
k = int(input('Введите число: '))
print(cnt(k))
