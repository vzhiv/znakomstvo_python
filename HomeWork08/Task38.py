# Задача №38 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def read_file(filename):
    with open('file.txt', 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(',')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    
    with open('file.txt', 'w') as data:
        for i in data_array:
            if i != []:
                write_item = ','.join(i)
                data.write(f'{write_item}\n')


def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print(f"ID: {data_array[i][0]} Фамилия: {data_array[i][1]} Имя: {data_array[i][2]} Отчество: {data_array[i][3]} Телефон: {data_array[i][4]} ")


def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    lastname = input('Введите фамилию и нажмите ENTER: ')
    firstname = input('Введите имя и нажмите ENTER: ')
    secondname = input('Введите отчество и нажмите ENTER: ')
    phone = input('Введите телефон и нажмите ENTER: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    data_array.append(new_item)
    write_file(filename, data_array)
    print('Запись успешно добавлена')

def find_item(filename):
    data_array = read_file(filename)
    find_data = input('Введите одно из значений для поиска (ID, Фамилия, Имя, Отчество, Номер телефона) и нажмите ENTER: ')
    temp = 0
    for i in range(1, len(data_array)):
        for j in range(5):
            if find_data == data_array[i][j]: 
                print(f"ID: {data_array[i][0]} Фамилия: {data_array[i][1]} Имя: {data_array[i][2]} Отчество: {data_array[i][3]} Телефон: {data_array[i][4]} ")
                temp += 1
    
    if temp != 0:
        print(f'Запись: {find_data} успешно найдена!')
    else:
        print(f'Запись: {find_data} не найдена!')

def change_item(filename):
    data_array = read_file(filename)
    while True:
        id_item = input('Для изменения записи, введите ID пользователя и нажмите ENTER: ')
        if id_item.isdigit() == False:
            print('Неверные данные, повторите ввод')
        else:
            break
    id_item = int(id_item)
    temp = 0

    for i in range(1, len(data_array)):
        if id_item == int(data_array[i][0]): 
            print(f"ID: {data_array[i][0]} Фамилия: {data_array[i][1]} Имя: {data_array[i][2]} Отчество: {data_array[i][3]} Телефон: {data_array[i][4]} ")
            user_operation = 0
            while user_operation != 6:
                while True:
                    print('Добро пожаловать в меню изменения записи!')
                    print('Введите 1 - Показать запись')
                    print('Введите 2 - Изменить фамилию')
                    print('Введите 3 - Изменить имя')
                    print('Введите 4 - Изменить отчество')
                    print('Введите 5 - Изменить номер телефона')
                    print('Введите 6 - Выход из меню изменения записи')
                    user_operation = input()
                    if user_operation.isdigit() == False or int(user_operation) <= 0 or int(user_operation) > 6:
                        print('Неверные данные, повторите ввод')
                    else:
                        break
            
                user_operation = int(user_operation)
                if user_operation == 1:
                    print(f"ID: {data_array[i][0]} Фамилия: {data_array[i][1]} Имя: {data_array[i][2]} Отчество: {data_array[i][3]} Телефон: {data_array[i][4]} ")
                elif user_operation == 2:
                    data_array[i][1] = input('Введите новую фамилию и нажмите ENTER: ')
                elif user_operation == 3:
                    data_array[i][2] = input('Введите новое имя и нажмите ENTER: ')
                elif user_operation == 4:
                    data_array[i][3] = input('Введите новое отчество и нажмите ENTER: ')
                elif user_operation == 5:
                    data_array[i][4] = input('Введите новый номер телефона и нажмите ENTER: ')
                
            write_file(filename, data_array)        
            temp += 1
    
    if temp != 0:
        print(f'Запись с ID: {id_item} успешно изменена!')
    else:
        print(f'Записи с ID: {id_item} не существует!')


def delete_item(file_item):
    data_array = read_file(filename)
    while True:
        id_item = input('Для удаления записи, введите ID пользователя и нажмите ENTER: ')
        if id_item.isdigit() == False:
            print('Неверные данные, повторите ввод')
        else:
            break
    id_item = int(id_item)
    temp = 0
    for i in range(1, len(data_array)):
        if id_item == int(data_array[i][0]): 
            data_array[i].clear()
            write_file(filename, data_array)
            temp += 1
    
    if temp == 1:
        print(f'Запись с ID: {id_item} успешно удалена!')
    else:
        print(f'Записи с ID: {id_item} не существует!')


def menu():
    user_operation = 0
    while user_operation != 6:
        while True:
            print('Добро пожаловать в телефонный справочник!')
            print('Введите 1 - Показать все записи')
            print('Введите 2 - Добавить запись')
            print('Введите 3 - Поиск записи')
            print('Введите 4 - Изменить запись')
            print('Введите 5 - Удалить запись')
            print('Введите 6 - Выход из справочника')
            user_operation = input()
            if user_operation.isdigit() == False or int(user_operation) <= 0 or int(user_operation) > 6:
                print('Неверные данные, повторите ввод')
                print('')
            else:
                break
        user_operation = int(user_operation)
        if user_operation == 1:
            show_all_items(filename)
        elif user_operation == 2:
            add_item(filename)
        elif user_operation == 3:
            find_item(filename)
        elif user_operation == 4:
            change_item(filename)
        elif user_operation == 5:
            delete_item(filename)
        

filename = 'file.txt'

menu()