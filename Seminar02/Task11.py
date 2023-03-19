# Задача №11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

while True:
    number = input('Введите натуральное число A > 1: ')
    if number.isdigit() == False or int(number) <= 1:
        print('Неверные данные, повторите ввод')
    else:
       break

number = int(number)
fibo_n = 0
fibo_n_1 = 1
fibo_n_2 = 1
n = 2

while fibo_n < number: 
    fibo_n = fibo_n_1 + fibo_n_2
    fibo_n_2 = fibo_n_1
    fibo_n_1 = fibo_n
    n += 1

if fibo_n == number:
    print(f"Число {number}, является числом Фибоначи и идет {n} по счету")
else:
    print(f"Число {number}, НЕ является числом Фибоначи")