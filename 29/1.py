import time


def timeResult(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func()
        dt = time.time() - st
        print(f'Время работы - {dt}')
        print(*result)

    return wrapper


@timeResult
def simpleNum():
    arr = list()
    for i in range(1000):
        count = 0
        for j in range(i + 1):
            if i != 0 and j != 0 and i % j == 0:
                count += 1
        if count == 2:
            arr.append(i)
    return arr


simpleNum()
