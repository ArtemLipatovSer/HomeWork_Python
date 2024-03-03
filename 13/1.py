one = (1, 2, 3, 4)
two = (5, 4, 6, 7, 2)
three = (5, 11, 2, 4, 6)
result = list()

for i in range(len(one)):
    if (one[i] in two) and (one[i] in three):
        result.append(one[i])

print(result)
