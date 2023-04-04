# Задача №43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:       Вывод:
# 1 2 3 2 3       2


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
        multi.append(random.randint(0, 3))

    print(multi)
    return multi


def FindCouple(mul):
    result = 0

    for i in range(len(mul)):
        for j in range(i+1,len(mul)):   
            if mul[i] == mul[j]:
                result += 1 

    return result

multi = list()


multi = FillRandom(set)

print(FindCouple(multi))