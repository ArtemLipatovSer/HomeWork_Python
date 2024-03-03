import time


def timeResult(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        dt = time.time() - st
        print(f'Время работы - {dt}')
        print(*result)

    return wrapper


@timeResult
def simpleNum(st, end):
    arr = list()
    for i in range(st, end):
        count = 0
        for j in range(i + 1):
            if i != 0 and j != 0 and i % j == 0:
                count += 1
        if count == 2:
            arr.append(i)
    return arr


simpleNum(1, 10000)
