strUser = input('Введите строку: ')
strUserRe = ''
strUser = strUser.replace(' ', '')
strUser = strUser.lower()
for i in range(len(strUser)-1, -1, -1):
    strUserRe += strUser[i]

if strUser == strUserRe:
    print('Строка палиндромом')
else:
    print('Строка обычная')

