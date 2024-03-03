def funMultiply(list):
    multi = 1
    for i in list:
        multi *= int(i)
    return multi


print(funMultiply(list('333')))
