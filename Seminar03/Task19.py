# Задача №19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

import random

while True:
    number = input('Введите количество элементов: ')
    sdvig = input('Введите количество элементов сдвига: ')
    if number.isdigit() == False or int(number) <= 0 or sdvig.isdigit() == False or int(sdvig) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

spisok = list()    

for i in range(int(number)):
    spisok.append(random.randint(0, 10))

print(spisok)

for i in range(int(sdvig)):
    temp = spisok.pop()
    spisok.insert(0, temp)

print(spisok)


# print(spisok[sdvig * -1:] + spisok[ :len(spisok) - sdvig])