# Задача №15
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

import random

while True:
    number = input('Введите общее количество арбузов: ')
    if number.isdigit() == False or int(number) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

weight_arbyz = list()    

for i in range(int(number)):
    weight_arbyz.append(random.randint(1, 30))

print(weight_arbyz)
min = weight_arbyz[0]
max = weight_arbyz[0]

for i in range(int(number)):
    if (int(weight_arbyz[i]) > max):
        max = weight_arbyz[i]
    if (int(weight_arbyz[i]) < min):
        min = weight_arbyz[i]

print(f'Самый тяжелый арбуз весит {max}')
print(f'Самый легкий арбуз весит {min}')