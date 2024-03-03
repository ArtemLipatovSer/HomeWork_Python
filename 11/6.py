def funDegree(list, deg):
    listRe = []
    for i in range(len(list)):
        listRe.append(list[i] ** deg)
    return listRe


arr = [1, 2, 3]

print(funDegree(arr, 2))

