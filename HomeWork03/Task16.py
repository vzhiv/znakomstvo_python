# Задача №16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

import random

while True:
    num = input('Введите количество элементов массива: ')
    number = input('Введите число которые вы хотите найти: ')
    if number.isdigit() == False or int(num) <= 0 or num.isdigit() == False or int(number) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

array = list()
num = int(num)
number = int(number)

array = [random.randint(1, num//2) for _ in range(int(num))]

print(array)
count = 0

for i in range(len(array)):
    if(number == array[i]):
        count += 1

print(f'Число {number} встречается в массиве {count} раз')