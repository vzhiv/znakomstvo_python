# Задача №2
# Найдите сумму цифр трехзначного числа. или любого

while True:
    number = input('Введите произвольное число: ')
    if number.isdigit() == False:
        print('Неверные данные, повторите ввод')
    else:
       break

number = int(number)
sum = 0
while number > 0: 
    sum = sum + number % 10
    number = number // 10

print(f"Сумма цифр =  {sum}")