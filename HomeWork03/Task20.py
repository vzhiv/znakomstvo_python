# Задача №20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы

while True:
    word = input('Введите слово на русском или английском языке: ')
    if word.isalpha() == False:
        print('Неверные данные, повторите ввод')
    else:
       break

word = word.upper()

dict_eng_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
dict_eng_2 = dict.fromkeys(['D', 'G'], 2)
dict_eng_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
dict_eng_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
dict_eng_5 = dict.fromkeys(['K'], 5)
dict_eng_8 = dict.fromkeys(['J', 'X'], 8)
dict_eng_10 = dict.fromkeys(['Q', 'Z'], 10)

dict_eng = { **dict_eng_1, **dict_eng_2, **dict_eng_3, **dict_eng_4, **dict_eng_5, **dict_eng_8, **dict_eng_10}

dict_rus_1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
dict_rus_2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
dict_rus_3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
dict_rus_4 = dict.fromkeys(['Й', 'Ы'], 4)
dict_rus_5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
dict_rus_8 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
dict_rus_10 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)

dict_rus = { **dict_rus_1, **dict_rus_2, **dict_rus_3, **dict_rus_4, **dict_rus_5, **dict_rus_8, **dict_rus_10}
# eng_key_list = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
# eng_value_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 8, 8, 10, 10]
# dict_eng = dict(zip(eng_key_list, eng_value_list))

# rus_key_list = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ']
# rus_value_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 8, 8, 8, 10, 10, 10]
# dict_rus = dict(zip(rus_key_list, rus_value_list))

cost = 0

for i in range(len(word)):
    if(ord(word[i]) >= 41 and ord(word[i]) <= 90):
        cost += dict_eng.get(word[i])
    else:
        cost += dict_rus.get(word[i])

print(f"Стоимость слова {word}, составляет {cost}")