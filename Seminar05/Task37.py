# Задача №37
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def super_recurse():
    number = input()
    if number != '':
        super_recurse()
    print(number)

super_recurse()


# num = [3, 4, 7 ,9]

# # num = sorted(num, reverse=True)

# # print(num)

# print(num[::-1])