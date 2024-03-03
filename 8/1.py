import random

rndOne = list()
rndTwo = list()
for i in range(5):
    rndOne.append(random.randint(1, 10))
    rndTwo.append(random.randint(1, 10))
print(rndOne)
print(rndTwo)

rndThree = list()
for i in range(len(rndOne)):
    rndThree.append(rndOne[i])
for i in range(len(rndTwo)):
    rndThree.append(rndTwo[i])
print(rndThree)

rndThree.clear()

for i in rndOne:
    if i not in rndThree:
        rndThree.append(i)
for i in rndTwo:
    if i not in rndThree:
        rndThree.append(i)

print(rndThree)

rndThree.clear()

for i in rndOne:
    for j in rndTwo:
        if i == j:
            rndThree.append(i)

print(rndThree)

rndThree.clear()

for i in rndOne:
    if i in rndThree:
        continue
    else:
        rndThree.append(i)
for i in rndTwo:
    if i in rndThree:
        continue
    else:
        rndThree.append(i)

print(rndThree)

rndThree.clear()

rndThree.append(min(rndOne + rndTwo))
rndThree.append(max(rndOne + rndTwo))

print(rndThree)
