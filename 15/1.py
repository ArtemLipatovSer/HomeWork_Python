words = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}

message = input('Введите предложение: ')
a = []

for i in message.upper():
    for key in words:
        count = 0
        for value in words[key]:
            count += 1
            if i == value:
                a.append(key * count)

result = ''.join(a)

print(result)



