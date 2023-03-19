# Задача №23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

import random

while True:
    number = input('Введите количество чисел: ')
    if number.isdigit() == False or int(number) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

array = [random.randint(-10, 10) for _ in range(int(number))]
print(array)
count = 0
str = ""

for i in range(len(array)-1):
    if(array[i] < array[i + 1]):
        count += 1
        str += f'{array[i]} < {array[i+1]}, '
        
print(f'{count} ({str})')