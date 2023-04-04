# Задача №30  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


import random

while True:
    first_el = input('Введите первый элемент прогрессии: ')
    numbers = input('Введите количество элементов прогрессии: ')
    diff = input('Введите шаг разности: ')
    if first_el.isdigit() == False or numbers.isdigit() == False or diff.isdigit() == False or int(numbers) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break


def FillArray(first, num, diff):
    array = [first]
    
    for i in range(2, num+1):
        array.append(first + (i - 1) * diff )

    return array


arr = list()


arr = FillArray(int(first_el), int(numbers), int(diff))

print(arr)