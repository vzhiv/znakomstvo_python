# Задача №17
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

while True:
    number = input('Введите количество элементов: ')
    if number.isdigit() == False or int(number) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

spisok = list()    

for i in range(int(number)):
    spisok.append(random.randint(1, 4))

print("Дан список", spisok)
set = set(spisok)
print("В нём содержится", len(set), "уникальных элементов")
