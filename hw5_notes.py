# 1. Написать функцию, которая проверяет, что переданное ей число больше 0
def check_is_positive(number: int) -> bool:
    if number > 0:
        return True
    else:
        return False


# print(check_is_positive(1))
# print(check_is_positive(-1))
# print(check_is_positive(0))
#
#
# def check_is_positive2(number: int) -> bool:
#     return number > 0
#
#
# print(check_is_positive2(1))
# print(check_is_positive2(-1))
# print(check_is_positive2(0))

# 2. Написать функцию, которая принимает список чисел и выводит их в формате:
# <число>: <положительное/отрицательное>, одна запись на одной строке.
# Использовать для проверки функцию из первого задания.


def print_numbers(numbers: list) -> None:
    for number in numbers:
        if number % 5 == 0:
            return
        result = "положительное" if check_is_positive(number) else "отрицательное"
        print(f'{number}: {result}')


############################## HW 5 ##############################


def is_even(number: int) -> bool:
    if type(number) != int:
        print('Ошибка! Введенные данные не являются числом')
        return False
    return number % 2 == 0


def print_numbers(n: int) -> None:
    if type(n) != int:
        print('Ошибка! Введенные данные не являются числом')
        return

    for num in range(1, n):
        if num % 7 == 0 and num % 4 == 0:
            return
        elif is_even(num):
            print(num ** 2)
        else:
            print(num)
