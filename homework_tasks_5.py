# 1
# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки

# 2
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.















# import json
#
#
# with open('example.json') as json_file:
#     data = json.load(json_file)
#
# print(data, type(data))
# data["is_developer"] = True
# with open('example.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

import csv

with open('example.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for i, row in enumerate(file_reader):
        if i == 0:
            columns_list = row
        else:
            print(row)
            for column_name, value in zip(columns_list, row):
                print(f'{column_name} is {value or None}')


with open('example.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Ann', 40, 'ann@email.com', None])
