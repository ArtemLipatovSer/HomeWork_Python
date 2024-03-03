worker1 = int(input('Введите уровень продаж первого работника: '))
worker2 = int(input('Введите уровень продаж второго работника: '))
worker3 = int(input('Введите уровень продаж третьего работника: '))

if worker1 < 500:
    salary1 = 200 + (200*0.03)
elif 500 < worker1 < 1000:
    salary1 = 200 + (200*0.05)
else:
    salary1 = 200 + (200*0.08)

if worker2 < 500:
    salary2 = 200 + (200*0.03)
elif 500 < worker2 < 1000:
    salary2 = 200 + (200*0.05)
else:
    salary2 = 200 + (200*0.08)

if worker3 < 500:
    salary3 = 200 + (200*0.03)
elif 500 < worker3 < 1000:
    salary3 = 200 + (200*0.05)
else:
    salary3 = 200 + (200*0.08)

if salary1 > salary2 and salary1 > salary3:
    salary1 = salary1 + 200
if salary2 > salary1 and salary2 > salary3:
    salary2 = salary2 + 200
if salary3 > salary2 and salary3 > salary1:
    salary3 = salary3 + 200

print(f'Зарплаты менеджеров - \n'
      f'Первый менеджер - {salary1}\n'
      f'Второй менеджер - {salary2}\n'
      f'Третий менеджер - {salary3}')
