# Задача №39
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

while True:
    set_1 = input('Введите количество элементов первого набора чисел: ')
    set_2 = input('Введите количество элементов второго набора чисел: ')
    if set_1.isdigit() == False or int(set_1) <= 0 or set_2.isdigit() == False or int(set_2) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break


def FillRandom(set):

    multi = list()
    for i in range(int(set)):
        multi.append(random.randint(0, 10))

    print(multi)
    return multi


def FindDiff(mul_1, mul_2):
    result = mul_1

    for i in range(len(mul_1)-1,-1, -1):
        for j in range(len(mul_2)):
            if mul_1[i] == mul_2[j]:
                result.pop(i)

                break

    return result

multi_1 = list()
multi_2 = list()


multi_1 = FillRandom(set_1)
multi_2 = FillRandom(set_2)

print(FindDiff(multi_1, multi_2))