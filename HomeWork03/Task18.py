# Задача №18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6


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

array = [random.randint(1, num) for _ in range(int(num))]
#array = [10 , 2 , 5 , 3, 9]
print(array)
raznost = number - array[0]
count = 0
index = 0

for i in range(len(array)):
    if(number == array[i]):
        raznost = 0
        index = i
    else:
        count = number - array[i]
        print(count, raznost)
        if count <= abs(raznost) and count > 0:
            raznost = count
            index = i
        if count > -raznost and count < 0:
            raznost = count
            index = i
        print(count, raznost)

print(f'Число {number} ближе всего к {array[index]}')