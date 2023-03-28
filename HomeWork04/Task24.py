# Задача №24 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

while True:
    bush = input('Введите количество кустов на грядке: ')
    if bush.isdigit() == False or int(bush) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

bush_berry = list()


for i in range(int(bush)):
    bush_berry.append(random.randint(0, 30))

print(bush_berry)

berry = 0
max_berry = 0
bush_i = 0

for i in range(len(bush_berry)):
    if(i == 0):
        berry = bush_berry[i] + bush_berry[i + 1] + bush_berry[len(bush_berry) - 1]
        if(berry > max_berry):
            max_berry = berry
            bush_i = i
    if (i == len(bush_berry) - 1):
        berry = bush_berry[i] + bush_berry[i - 1] + bush_berry[0]
        if(berry > max_berry):
            max_berry = berry
            bush_i = i
    else:
        berry = bush_berry[i] + bush_berry[i - 1] + bush_berry[i + 1]
        if(berry > max_berry):
            max_berry = berry
            bush_i = i
print(f'Максимальное количество ягод будет перед кустом {bush_i + 1} и состовляет {max_berry}')