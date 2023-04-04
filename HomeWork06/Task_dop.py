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


def InputData():
    while True:
        step = input('Введите номер свободной ячейки для хода (от 1 до 9): ')
        if step.isdigit() == False or int(step) <= 0 or int(step) >= 10 :
            print('Неверные данные, повторите ввод')
        else:
            return step

def Print_Field(arr):
    print(f'{arr[0]} | {arr[1]} | {arr[2]}')
    print(f'---------')
    print(f'{arr[3]} | {arr[4]} | {arr[5]}')
    print(f'---------')
    print(f'{arr[6]} | {arr[7]} | {arr[8]}')





def CheckCell(arr, step):
    if arr[step] != " ":
        print('Ячейка занята, повторите ввод')
        return False
    else:
        return True



def CheckWin(arr):
    result = 0
    if (arr[0] == "X" and arr[1] == "X" and arr[2] == "X"):
        result = 1 
    elif (arr[3] == "X" and arr[4] == "X" and arr[5] == "X"):
        result = 1
    elif (arr[6] == "X" and arr[7] == "X" and arr[8] == "X"):
        result = 1
    elif (arr[0] == "X" and arr[3] == "X" and arr[6] == "X"):
        result = 1
    elif (arr[1] == "X" and arr[4] == "X" and arr[7] == "X"):
        result = 1
    elif (arr[2] == "X" and arr[5] == "X" and arr[8] == "X"):
        result = 1
    elif (arr[0] == "X" and arr[4] == "X" and arr[8] == "X"):
        result = 1
    elif (arr[2] == "X" and arr[4] == "X" and arr[6] == "X"):
        result = 1
    elif (arr[0] == "O" and arr[1] == "O" and arr[2] == "O"):
        result = 2 
    elif (arr[3] == "O" and arr[4] == "O" and arr[5] == "O"):
        result = 2
    elif (arr[6] == "O" and arr[7] == "O" and arr[8] == "O"):
        result = 2
    elif (arr[0] == "O" and arr[3] == "O" and arr[6] == "O"):
        result = 2
    elif (arr[1] == "O" and arr[4] == "O" and arr[7] == "O"):
        result = 2
    elif (arr[2] == "O" and arr[5] == "O" and arr[8] == "O"):
        result = 2
    elif (arr[0] == "O" and arr[4] == "O" and arr[8] == "O"):
        result = 2
    elif (arr[2] == "O" and arr[4] == "O" and arr[6] == "O"):
        result = 2

    return result


field = [" "," "," "," "," "," "," "," "," "]
count = 0
step_human = 0

while count < 9:
    while True:
        step_human = int(InputData())
        if CheckCell(field,step_human - 1) == True:
            break

    

    if CheckCell(field, step_human-1) == False:
        count -= 1
    else:
        field[step_human-1] = "X"
    Print_Field(field)
    count += 1
    if CheckWin(field) == 1:
        print("Победил человек")
        break
    
    for i in range(len(field)):
        if field[i] == " ":
            field[i] = "O"
            count += 1
            break
    print("Ход компьютера")
    Print_Field(field)
    if CheckWin(field) == 2:
        print("Победил компьютер")
        break
    
        
if count == 9 and CheckWin(field) == 0:
    print("Ячейки закончились. НИЧЬЯ")