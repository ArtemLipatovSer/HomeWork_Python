def list_sorted(func):
    def wrapper(list):
        return sorted(func(list))

    return wrapper


@list_sorted
def get_list(s):
    arr = list(map(int, s.split()))
    return arr


lst = get_list('3 2 1 -2')
print(*lst)
