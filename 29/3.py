def report(organization):
    def dec(func):
        def wrapper(*args, **kwargs):
            if organization == 'mail':
                print('Отчет для организации Mail')
                func()
            elif organization == 'google':
                print('Отчет для организации Google')
                func()

        return wrapper

    return dec


@report('mail')
def reportOne():
    print('Сам отчет!!!')


@report('google')
def reportTwo():
    print('Сам отчет!!!')


reportOne()
reportTwo()
