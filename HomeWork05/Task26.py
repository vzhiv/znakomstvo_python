# Задача №26  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def Degree(num , deg):
    if(deg > 0): 
        return Degree(num, deg - 1) * num
    elif(deg < 0):
        return 1 / (Degree(num, - deg - 1) * num)
    else:
        return 1



while True:
    num_1 = input('Введите число которое будем возводить в степень: ')
    num_2 = input('Введите степень в которую будем возводить число: ')
    if num_1.isdigit() == False or num_2.lstrip("-").isdigit() == False or int(num_1) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

print(Degree(int(num_1) , int(num_2)))