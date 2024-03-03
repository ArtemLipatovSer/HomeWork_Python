def show_menu(func):
    def wrapper(list):
        for i in range(len(func(list))):
            print(f'{i + 1}. {(func(list)[i]).title()}')

    return wrapper


@show_menu
def get_menu(s):
    arr = []
    arr = s.split(' ')
    return arr


