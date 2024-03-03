def funcMulti(a,b):
    multi = 1
    if a > b:
        for i in range(b, a+1):
            multi *= i
    else:
        for i in range(a,b+1):
            multi *= i
    return multi


print(funcMulti(5, 1))
