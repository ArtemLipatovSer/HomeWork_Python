numOne = int(input("Введите зарплату за месяц: "))
numTwo = int(input("Введите сумму месячного платежа по кредиту в банке: "))
numThree = int(input("Введите задолженность за коммунальные услуги: "))

print(f'Оставшееся сумма - {numOne - numTwo - numThree}')
