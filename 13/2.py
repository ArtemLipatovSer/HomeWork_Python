one = (1, 2, 3, 4)
two = (5, 4, 6, 7, 2)
three = (5, 11, 2, 4, 6)
result = list()

for i in range(len(one)):
    if (one[i] not in two) and (one[i] not in three):
        result.append(one[i])
for i in range(len(two)):
    if (two[i] not in one) and (two[i] not in three):
        result.append(two[i])
for i in range(len(three)):
    if (three[i] not in one) and (three[i] not in two):
        result.append(three[i])

print(result)
