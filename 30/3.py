import json


class Shape:
    figures = []

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

        self.figures.append(self.__dict__)

    def show(self):
        pass

    @staticmethod
    def save():
        with open('Figure.json', 'w', encoding='utf-8') as file:
            json.dump(Shape.figures, file, ensure_ascii=False, indent=2)

    @staticmethod
    def load():
        with open('Figure.json', encoding='utf-8') as file:
            return file.read()


class Square(Shape):
    def __init__(self, name, x, y, a):
        super().__init__(name, x, y)
        self.a = a

    def show(self):
        print(f'Фигура - {self.name}, координаты левого верхнего угла - {self.x, self.y}, '
              f'длина стороны - {self.a}')


class Rectangle(Shape):
    def __init__(self, name, x, y, a, b):
        super().__init__(name, x, y)
        self.a = a
        self.b = b

    def show(self):
        print(f'Фигура - {self.name}, координаты левого верхнего угла - {self.x, self.y}, '
              f'длины сторон: a - {self.a}, b - {self.b}')


class Circle(Shape):
    def __init__(self, name, x, y, r):
        super().__init__(name, x, y)
        self.r = r

    def show(self):
        print(f'Фигура - {self.name}, координаты центра - {self.x, self.y}, '
              f'радиус - {self.r}')


class Ellipse(Shape):
    def __init__(self, name, x, y, a, b):
        super().__init__(name, x, y)
        self.a = a
        self.b = b

    def show(self):
        print(f'Фигура - {self.name}, координаты верхнего угла описанного вокруг него прямоугольника со сторонами, '
              f'параллельными осям координат - {self.x, self.y}, '
              f'длины сторон прямоугольника: a - {self.a}, b - {self.b}')


one = Square('Квадрат', 2, 3, 4)
two = Rectangle('Прямоугольник', 3, 4, 6, 3)
three = Circle('Окружность', 2, 3, 7)
four = Ellipse('Эллипс', 2, 2, 4, 5)

print(Shape.figures)

Shape.save()

figures_new = Shape.load()
print(figures_new)

one.show()
two.show()
three.show()
four.show()
