# file = open('hello.txt')
# # тут работаем с файлом
# file.close()
#
#
# with open('hello.txt') as file:
#     # тут работаем с файлом
#     pass

# 1. после with писать самому file.close()
# 2. мы не можем работать с файлом вне блока with

# первое задание
# var1 = '1'
# var2 = '1'
# var3 = '1'
# var4 = '1'
# with open('new_file.txt', 'w') as file:
#     file.write(var1 + '\n')
#     file.write(var2 + '\n')
# with open('new_file.txt', 'a') as file:
#     file.write(var3 + '\n')
#     file.write(var4 + '\n')


# 2
import json

my_dict = {
    123456: ('name', 12),
    103456: ('name2', 12),
    129856: ('name3', 12),
    123156: ('name12', 12),
    111116: ('name4', 12),
    155556: ('name5', 12),
}
with open('dict.json', 'w') as file:
    json.dump(my_dict, file)


# 3
import csv
import random

with open('dict.json') as file:
    json_data = json.load(file)

with open('result.csv', 'w', encoding='utf-8') as file:
    columns = ['id', 'name', 'age', 'телефон']
    # file.write(','.join(columns) + '\n')

    writer = csv.writer(file)
    writer.writerow(columns)
    for item_key in json_data:
        # json_data[item_key] = value = ('name', 12)
        writer.writerow([item_key, *json_data[item_key], random.randint(1, 10)])


# CLI - command line interface
