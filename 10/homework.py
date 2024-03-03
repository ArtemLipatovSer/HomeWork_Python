check = int(input("Выберите вариант: \n"
                  "А - цифра 1\n"
                  "Б - цифра 2\n"
                  "В - цифра 3\n"
                  "Г - цифра 4\n"
                  "Д - цифра 5\n"
                  "Е - цифра 6\n"
                  "Ж - цифра 7\n"
                  "З - цифра 8\n"
                  "И - цифра 9\n"
                  "К - цифра 10\n---> "))
# Вариант А:
if check == 1:
    count = 5
    for j in range(0, 6, 1):
        print(j*'   ', end='')
        for i in range(count, 0, -1):
            print(count*' * ')
            count -= 1
            break

# Вариант Б:
if check == 2:
    for i in range(1, 6, 1):
        print(i * ' * ')

# Вариант В:
if check == 3:
    count = 5
    for j in range(0, 6, 1):
        print(j*'   ', end='')
        for i in range(count, 0, -1):
            print(count*' * ', end='')
            for h in range(count, 0, -1):
                print(count * ' * ')
                count -= 1
                if count == 0:
                    print((j+3)*'  ', '* ')
                break
            break

# Вариант Г:
if check == 4:
    count = 1
    for j in range(5, 0, -1):
        if j == 5:
            print((j-2)*'\t', ' ', '*')
        if j  >  1:
            print((j-1)*'   ', end='')
        for i in range(count):
            print(count*' * ', end='')
            for h in range(count):
                print(count * ' * ')
                count += 1
                break
            break

# Вариант Д:
if check == 5:
    count = 5
    for j in range(0, 6, 1):
        print(j * '   ', end='')
        for i in range(count, 0, -1):
            print(count * ' * ', end='')
            for h in range(count, 0, -1):
                print(count * ' * ')
                count -= 1
                if count == 0:
                    print((j + 3) * '  ', '* ')
                break
            break
    count = 1
    for j in range(5, 0, -1):
        if j == 5:
            print('*')
        if j > 1:
            print((j - 1) * '   ', end='')
        for i in range(count):
            print(count * ' * ', end='')
            for h in range(count):
                print(count * ' * ')
                count += 1
                break
            break

# Вариант E:
if check == 6:
    count = 4
    index = 1
    for i in range(1, 6):
        print(i*' * ', end='')
        for j in range(1):
            print(count * '   ', end='')
            for h in range(1):
                print(count * '   ', end='')
                count -= 1
                for g in range(1):
                    print(index*' * ')
                    index += 1
    count = 5
    index = 0
    for i in range(5, 0, -1):
        print(i*' * ', end='')
        for h in range(1):
            print(index*'   ', end='')
            for j in range(1):
                print(count * ' * ')
        count -= 1
        index += 2

# Вариант Ж:
if check == 7:
    for i in range(1, 6):
        print(i*' * ')
    for i in range(6, 0, -1):
        print(i*' * ')

# Вариант З:
if check == 8:
    count = 1
    index = 5
    for i in range(5, 0, -1):
        print(i*' - ', end='')
        for j in range(1):
            print(count*' * ')
        count += 1
    for i in range(1, 6):
        print(i*' - ', end='')
        for j in range(1):
            print(index*' * ')
        index -= 1

# Вариант И:
if check == 9:
    for i in range (5, 0, -1):
        print(i*' * ')

# Вариант К:
if check == 10:
    index = 1
    for i in range(5, 0, -1):
        print(i*'   ', end='')
        for j in range(1):
            print(index*' * ')
        index += 1

