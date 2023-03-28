# Задача №27
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
import fileinput

with open('D:/!ОБУЧЕНИЕ/Основное обучение/Знакомство с языком Python (семинары)/Seminar04/1.txt', encoding='utf-8') as f:
    string = f.read().lower().strip().split()

print(len(string))


dictionary = {}

for i in range(len(string)):
    if(string[i] in dictionary):
        dictionary[string[i]] += 1
    else:
        dictionary[string[i]] = 0


print(len(dictionary))
print(dictionary)

f.close()