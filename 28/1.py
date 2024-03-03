def func_show(func):
    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')

    return wrapper


def get_sq(width, height):
    square = width * height
    return square


f = func_show(get_sq)
f(4, 4)
