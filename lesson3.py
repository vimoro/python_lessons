# num = int(input())
# print(num)
# print(type(num))

# num1 = 5
# num2 = 2
# print(int(2.8))

# num = float(2)
# print(num)

# print(bool(1))
# print(bool(0))
# print(bool(0.0))
# print(bool(0.5))
# print(bool(int(0.5)))
# print(bool(256))
# print(bool(-256))

# print(bool("123"))
# print(bool(""))
# print(bool(" "))
#
# print(bool([1]))
# print(bool([]))
# print(bool([set()]))
# print(bool([0]))

# print(bool({'a': 1}))
# print(bool({}))

# num1 = 1
# num2 = 2
# print(str(num1) + str(num2))
# print(str(num1 + num2))
# print(str([1, 2, 3]))

# list, tuple
# list_ = list("abc")
# print(id(list_))
# list_ = list({1, 2, 3})
# list_2 = list(list_)
# print(id(list_))
# list_2.append("d")
# # print(list_)
# # print(list_2)
#
# list_3 = list_2[:]
# print(id(list_3))
# print(list_3)

# tuple_ = tuple("123")
# d = {1: 'a', 2: 'b'}
# print(d.keys())
# tuple_ = tuple(d)
# list_ = list(d)
# print(tuple_)
# print(list_)

# friends_phone_numbers = {
#     'Egor': 123,
#     'Liza': 555,
#     'Vanya': 908,
#     'Yana': 150,
# }
# friends_names = list(friends_phone_numbers)
# print(friends_names)
# del friends_names[1]
# friends_names.remove('Liza')
# friends_names.pop(1)
# print(friends_names)

# friends_names.append('Artem')
# print(friends_names)
# friends_names.insert(1, 'Artem')
# print(friends_names)

# friends_names[1] = 'Artem'
# print(friends_names)

######################### Тема 3 ##################################

# num = 1
# num += 2
# print(num)
#
# string = "abc"
# string += "d"
# print(string)

# list_ = [1, 2, 3]
# list_2 = [4, 5, 6]
# print(list_ + list_2)
# string = "abc"
# string2 = "de"
# print(string + string2)

# list_ = [1, 2, 3]
# list_2 = [1, 2, 3] * 2
# list_ *= 2
# print(list_)
# print(list_2)
#

# from copy import deepcopy
#
#
# list_ = [1, 2, [1]]
# list_3 = list_[:]
# list_4 = list(list_)
# # list_2 = list_ * 2
# list_2 = list_ + deepcopy(list_)
# # print(list_)
# # print(list_2)
# # print(list_[2])
# # list_[2] += [5]
# list_[2].append(5)
# print('initial', list_)
# print('after append', list_2)

# string = "abc"
# num = 2
# print(string + num)
# friends = {'Liz', 'Ann'}
# string += friends

# list_ = [1.3, 2.7, 6]
#
# print(sum(list_))
# print(max(list_))
# print(min(list_))

list_ = ["c", "b", "a"]
result = "-".join(list_)
hello_str = "hello"
result = 2 + 3
list_ = [1, 2, 3]

# print(f'My joint string is {list_} bla bla')
# print(f'My joint string is {result}[]I()$# bla bla')

# template = 'My joint {} string bla bla'
# print(template.format(result))
# print(template.format(hello_str))

#########################################
# if, elif, else
# num1 = int(input('num1: '))
# num2 = int(input('num2: '))

# is_bigger = num1 > num2
# print(is_bigger)

# and or
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# True or False = True
# False or True = True
# True or True = True
# False or False = False

# False or False or True = True
# False and False = False -> False or True = True
# False and False = False -> False and True = False
# if (num2 < num1 < 0) and (num2 > 0):
#     print(f'{num1} bigger {num2}')
# elif num1 < num2:
#     print(f'{num1} smaller {num2}')
# else:
#     print(f'{num1} = {num2}')
# if num1 + num2 == 5:
#     print(f'{num1} + {num2} = 5')

num = 0
result_str = str(num) if num else "empty"  # тернарный оператор
# print(bool(num))
# if num:
#     result_str = str(num)
# else:
#     result_str = "empty"

# print(result_str)
# print(type(result_str))

list_ = [5]
result_str = str(list_) if list_ else "empty"  # тернарный оператор

print(result_str)
print(type(result_str))
