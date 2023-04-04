# Задача №41
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)


import random

while True:
    set = input('Введите количество элементов набора чисел: ')
    if set.isdigit() == False or int(set) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break


def FillRandom(set):

    multi = list()
    for i in range(int(set)):
        multi.append(random.randint(0, 10))

    print(multi)
    return multi


def FindElement(mul):
    result = 0

    for i in range(1, len(mul)-1):
        if mul[i] > mul[i-1] and mul[i] > mul[i+1]:
            result += 1 

    return result

multi = list()


multi = FillRandom(set)

print(FindElement(multi))