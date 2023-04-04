# Задача №32 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


import random

while True:
    numbers = input('Введите количество элементов массива: ')
    min = input('Введите нижнюю границу диапазона: ')
    max = input('Введите верхнюю границу диапазона: ')
    if min.lstrip("-").isdigit() == False or numbers.isdigit() == False or max.lstrip("-").isdigit() == False or int(numbers) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

def FillRandom(num):

    arr = list()
    for i in range(int(num)):
        arr.append(random.randint(-30, 30))

    print(arr)
    return arr

def FindIndex(arr, min, max):
    index = []
    for i in range(len(arr)):
        if arr[i] < max and arr[i] > min:
            index.append(i)


    return index


array = list()


array = FillRandom(numbers)

print(FindIndex(array, int(min), int(max)))