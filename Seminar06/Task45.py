# Задача №45
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:       Вывод:
# 300         220 284

import math


while True:
    number = input('Введите число не превышающее 10^5: ')
    if number.isdigit() == False or int(number) <= 0 or int(number) > 10**5:
        print('Неверные данные, повторите ввод')
    else:
       break

def FindFriendlyNumber(num):

    for i in range(2, num+1):
        sum_del = 0
        for j in range (1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                sum_del += j
                if j != 1 and (i/j) != j:
                    sum_del += int(i / j)
        sum_del_2 = 0
        for k in range (1, int(math.sqrt(sum_del)) + 1):
            if sum_del % k == 0:
                sum_del_2 += k
                if k != 1 and (sum_del / k) != k:
                    sum_del_2 += int(sum_del / k)
        if(sum_del_2 == i and sum_del > sum_del_2):
            print(f"{sum_del_2} {sum_del}")



FindFriendlyNumber(int(number))


# 2 вариант

# def get_mul(number:int) -> list:
#     ls = []
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             ls.append(i)
#             if not ls.__contains__(number / i) and i != 1:
#                 ls.append(int(number / i))
#     return ls

# print(get_mul(36))

# for i in range(1, int(number)):
#     s = sum(get_mul(i))
#     if i == sum(get_mul(s)) and i < s:
#         print(f'{i} {s}')




