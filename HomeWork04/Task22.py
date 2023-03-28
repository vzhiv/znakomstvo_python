# Задача №22 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

while True:
    set_1 = input('Введите количество элементов первого набора чисел: ')
    set_2 = input('Введите количество элементов второго набора чисел: ')
    if set_1.isdigit() == False or int(set_1) <= 0 or set_2.isdigit() == False or int(set_2) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

multi_1 = list()
multi_2 = list()


for i in range(int(set_1)):
    multi_1.append(random.randint(0, 10))

for i in range(int(set_2)):
    multi_2.append(random.randint(0, 10))

print(multi_1)
print(multi_2)

result = sorted(set(multi_1).intersection(multi_2))


print(result)