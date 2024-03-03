one = (1, 2, 3, 4, 3)
two = (5, 2, 6, 7, 3)
three = (5, 2, 2, 4, 3)
result = list()

for i in range(len(one)):
    if (one[i] == two[i]) and (one[i] == three[i]):
        result.append(one[i])

print(result)
