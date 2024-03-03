class Drob:
    result = 0

    def __init__(self, chisl, znam):
        self.chisl = chisl
        self.znam = znam
        Drob.result += 1

    @staticmethod
    def methodRes():
        return Drob.result


obj = Drob(1, 2)
obj1 = Drob(2, 3)
obj2 = Drob(3, 5)
obj3 = Drob(3, 7)

print(obj.methodRes())
