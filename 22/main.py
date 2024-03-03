import json


# Запись
def recordEmployee(path):
    employee = {}
    check = 0
    while check != 2:
        lastName = input("Введите фамилию сотрудника: ")
        firstName = input("Введите имя сотрудника: ")
        age = input("Введите возраст сотрудника: ")
        check = int(input('Хотите продолжить? \n'
                          '1 - Да\n'
                          '2 - Нет '))
        employee[lastName] = {'firstName': firstName, 'age': age}

    try:
        with open(path, 'r+') as file:
            part = json.load(file)
            part.update(employee)
        with open(path, 'w') as file:
            json.dump(part, file)

    except:
        with open(path, 'w+') as file:
            json.dump(employee, file)


# Редактирование
def editingEmployees(path):
    editingLastName = input('Введите фамилию сотрудника, данные которого нужно отредактировать:\n')
    firstName = input('Введите новое имя сотрудника\n')
    age = input('Введите новый возраст сотрудника:\n')

    with open(path, 'r') as file:
        arr = json.load(file)
    for key, value in arr.items():
        if key == editingLastName:
            arr[key]['firstName'] = firstName
            arr[key]['age'] = age

    with open(path, 'w') as file:
        json.dump(arr, file)


# Удаление сотрудника:
def delEmployee(path):
    employee = input('Введите сотрудника, которого хотите удалить:\n')
    with open(path, 'r') as file:
        arr = json.load(file)
        del arr[employee]
    with open(path, 'w') as file:
        json.dump(arr, file)


# Поиск сотрудника:
def findEmployee(path):
    result = {}

    findParam = int(input('Выберете параметры поиска:\n'
              '1. По фамилию\n'
              '2. По возрасту\n'
              '3. По первой букве фамилии\n'))

    if findParam == 1:
        findEmp = input('Введите фамилию сотрудника:\n')
        with open(path, 'r') as file:
            file = json.load(file)
            for key, value in file.items():
                if key == findEmp:
                    result[key] = value
                    print(result)
            if result == {}:
                result = 'There are no such employees'
                print('*'*5, result, '*'*5)
                return 0

    elif findParam == 2:
        findEmp = input('Введите возраст сотрудника сотрудника:\n')
        with open('employees.json', 'r') as file:
            file = json.load(file)
            for key, value in file.items():
                if file[key]['age'] == findEmp:
                    result[key] = value
                    print(result)

            if result == {}:
                result = 'There are no such employees'
                print('*'*5, result, '*'*5)
                return 0

    elif findParam == 3:
        findEmp = input('Введите первую букву фамилии сотрудника:\n')
        with open('employees.json', 'r') as file:
            file = json.load(file)
            for key, value in file.items():
                if key[0] == findEmp:
                    result[key] = value
                    print(result)

            if result == {}:
                result = 'There are no such employees'
                print('*'*5, result, '*'*5)
                return 0

    else:
        print('error')
        return findEmployee(path)

    with open('resultFind.json', 'w') as file:
        json.dump(result, file)


if __name__ == '__main__':
    FILENAME = 'employees.json'
    print('*' * 5, 'Программа по работе с базой сотрудников', '*' * 5)
    check = int(input('Выберите действие:\n'
                      '1. Записать новые данные:\n'
                      '2. Редактировать данные:\n'
                      '3. Удаление сотрудника\n'
                      '4. Поиск и вывод сотрудников\n'))

    if check == 1:
        recordEmployee(FILENAME)
    elif check == 2:
        editingEmployees(FILENAME)
    elif check == 3:
        delEmployee(FILENAME)
    elif check == 4:
        findEmployee(FILENAME)
    else:
        print('error')




