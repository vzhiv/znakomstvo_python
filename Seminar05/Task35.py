# Задача №35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
import math

def simple(num):
    i = 2
    flag = 1
    if num == 1:
        return True
    else:
        while i <= math.sqrt(num):
            if num % i == 0:
                
                flag = 0
                break
                #return False
            i += 1
        #return True
        
    if flag == 0:
        print('Числое не простое')
    else:
        print('Числое простое')
    # count = 0
    # for i in range(1, num+1):
    #     if (num % i == 0):
    #         count += 1
    #         print(count)
    # if count == 1:
    #     return True
    # else:
    #     return False

    
while True:
    number = input('Введите число: ')
    if number.isdigit() == False:
        print('Неверные данные, повторите ввод')
    else:
       break


#print(simple(int(number)))
simple(int(number))