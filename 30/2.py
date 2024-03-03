class Figure:
    result = 0

    def square(self):
        pass

    def __int__(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        self.result = self.a * self.b
        return self.result

    def __str__(self):
        return f'Прямоугольник, сторона a = {self.a}, сторона b = {self.b}. ' \
               f'Площадь фигуры равна {int(self.square())}'


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def square(self):
        self.result = 3.14 * (self.r ** 2)
        return self.result

    def __str__(self):
        return f'Круг, радиус = {self.r}. Площадь фигуры равна {int(self.square())}'


class Right_triangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        self.result = (self.a * self.b) / 2
        return self.result

    def __str__(self):
        return f'Прямоугольник треугольник, сторона a = {self.a}, основание = {self.b}. ' \
               f'Площадь фигуры равна {int(self.square())}'

class Trapezoid(Figure):

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def square(self):
        self.result = ((self.a + self.b) * self.h) / 2
        return self.result

    def __str__(self):
        return f'Прямоугольник, сторона a = {self.a}, основание = {self.b}, высота = {self.h}. ' \
               f'Площадь фигуры равна {int(self.square())}'


a = Rectangle(4, 10)
b = Circle(5)
c = Right_triangle(2, 3)
d = Trapezoid(2, 10, 3)

print(a)
print(b)
print(c)
print(d)
