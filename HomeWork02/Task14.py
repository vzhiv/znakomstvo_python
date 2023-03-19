# Задача №14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    number = input('Введите число > 0: ')
    if number.isdigit() == False or int(number) < 0:
        print('Неверные данные, повторите ввод')
    else:
       break

number = int(number)
temp = 0
k = 0

while temp <= number:
    temp = 2**k
    k += 1
    if(temp <= number):
        print(temp)

