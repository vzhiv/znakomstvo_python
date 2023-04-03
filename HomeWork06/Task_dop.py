# Реализовать консольную игру в крестики-нолики.
# Условия:
# - Игровое поле одномерный массив с номерами ячеек [1,2,3,4,5,6,7,8,9]
# - Ход пользователя осуществляется путем ввода номера свободной ячейки
# .

# Примерный алгоритм:
# .

# check (вспомогательная функция)
# Есть ли уже выигрышная комбинация?
# Если есть, то функция должна вернуть кто выиграл - Х или О

# .

# while Пока никто не выиграл или пока не закончились свободные поля
# input Запросить у пользователя номер ячейки для хода
# Ход пользователя - поместить в указанный номер ячейки символ Х
# Ход компьютера - поместить в первую свободную ячейку символ О
# if check - проверка показала, что есть выигрышная комбинация
# Печатаем кто выиграл
# Прерываение цикла