# Задача №10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

while True:
    coin = input('Введите общее количество монет: ')
    if coin.isdigit() == False or int(coin) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

coins = list()    

for i in range(int(coin)):
    coins.append(random.randint(0, 1))

print(coins)

if(coin == 1):
    print('Ничего переворачивать не нужно')
else:
    orel = 0
    reshka = 0
    for i in range(int(coin)):
        if (int(coins[i]) > 0):
            reshka += 1
        else:
            orel += 1 
    if (orel == 0 or reshka == 0):
        print('Ничего переворачивать не нужно')
    elif(orel > reshka):
        print(f'Нужно перевернуть {reshka} монеток')
    elif(orel < reshka):
        print(f'Нужно перевернуть {orel} монеток')
    else:
        print(f'Минимальное количество перевората монеток одинаковое для люлбого варианта и равно {orel}')
