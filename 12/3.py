def square(side, simb, z):
    a = side

    if z:
        for i in range(side):
            print(side * simb)
            
    if not z:
        for i in range(side):
            if i == 0:
                print(side * simb)
            if side - 1 > i > 0:
                print(simb, (side + 2) * ' ', simb)
            if i + 1 == side:
                print(side * simb)


square(5, ' * ', False)
