from os import strerror

try:
    with open('files/text3.txt', 'r') as file:
        lines = file.readlines()
    with open('files/text3_1.txt', 'w') as file:
        for line in lines:
            if line != lines[len(lines)-1]:
                file.write(line)
except IOError as e:
    print(strerror(e.errno))






