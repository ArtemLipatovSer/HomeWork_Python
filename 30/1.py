class Figure:
    result = 0

    def square(self):
        pass


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        self.result = self.a * self.b
        return f'Пощадь прямогульника = {self.result}'


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def square(self):
        self.result = 3.14 * (self.r ** 2)
        return f'Пощадь круга = {self.result}'


class Right_triangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        self.result = (self.a * self.b) / 2
        return f'Пощадь прямоугольного треугольника = {self.result}'


class Trapezoid(Figure):

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def square(self):
        self.result = ((self.a + self.b) * self.h) / 2
        return f'Пощадь трапеции = {self.result}'


a = Rectangle(4, 10)
b = Circle(5)
c = Right_triangle(2, 3)
d = Trapezoid(2, 10, 3)

print(a.square())
print(b.square())
print(c.square())
print(d.square())
