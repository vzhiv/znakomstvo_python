# Задача №28 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
#Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def Summa(num_a , num_b):
    i = 1
    if(num_a >= num_b):
        if(num_b > 0):
            #print(num_b)
            #print(num_a) 
            return Summa(num_a + 1, num_b - 1)
        else:
            return num_a

    else:
        if(num_a > 0):
            return Summa(num_a - 1, num_b + 1)
        else:
            return num_b
        


while True:
    num_1 = input('Введите 1-е число: ')
    num_2 = input('Введите 2-е число: ')
    if num_1.isdigit() == False or num_2.isdigit() == False or int(num_1) <= 0 or int(num_2) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

print(f'Сумма чисел {num_1} и {num_2} = {Summa(int(num_1) , int(num_2))}')