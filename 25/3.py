class Metr:
    @staticmethod
    def mil(numb):
        return f'В 1 миле 1.609 километров\n{(numb / 1.609)} миль\n'

    @staticmethod
    def km(numb):
        return f'В 1 километре 0,621371 миль\n{numb * 1.609} километров\n'


# Из миль в километры
print(Metr.km(100))

# Из километров в мили
print(Metr.mil(100))
