# Задача №09
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

while True:
    number = input('Введите целое неотрицательное цисло: ')
    if number.isdigit() == False or int(number) < 0:
        print('Неверные данные, повторите ввод')
    else:
       break

number1 = int(number)
factorial = 1

while number1 > 0: 
    factorial *= number1
    number1 -= 1

print(f"Факториал числа {number} = {factorial}")





