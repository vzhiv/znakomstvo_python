# Задача №33
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

while True:
    num_score = input('Введите количество оценок в журнале: ')
    if num_score.isdigit() == False or int(num_score) <= 0:
        print('Неверные данные, повторите ввод')
    else:
       break

score = list()


for i in range(int(num_score)):
    score.append(random.randint(1, 5))

print(score)

max_score = max(score)#score[0]
min_score = min(score)#score[0]



# for i in range(len(score)):
#     if(score[i] > max_score):
#         max_score = score[i]
#     if(score[i] < min_score):
#         min_score = score[i]

for i in range(len(score)):
    if(score[i] == max_score):
        score[i] = min_score

print(score)