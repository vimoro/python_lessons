# 1
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}
# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

from typing import Callable
from datetime import datetime


class decorator:
    def __init__(self, func: Callable) -> Callable:
        self.func = func

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            print(f'Функция add вызвана в {datetime.now()} без параметров')
        elif args and not kwargs:
            print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args}')
        elif not args and kwargs:
            print(f'Функция add вызвана в {datetime.now()} c именованными параметрами {kwargs}')
        elif args and kwargs:
            print(f'Функция add вызвана в {datetime.now()} c позиционными параметрами {args} и с именнованными парметрами {kwargs}')
        return self.func(*args, **kwargs)


@decorator
def add(*args, **kwargs):
    return 100


print(add())
print(add(1, 3))
print(add(a=1, b=3))
print(add(1, b=3))


# Добавить обработку исключений в следующие задания:
    # 2 (из ДЗ номер 5)
    # Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
    # Если число является четным, вывести квадрат числа, вместо числа.
    # Если число делится на 7 и на 4 одновременно, процесс останавливается.
    # Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.


def check_is_even(num: int) -> bool:
    return num % 2 == 0


def print_nums(n: int) -> None:
    for num in range(0, n):
        if num % 7 == 0 and num % 4 == 0 and num != 0:
            return
        elif check_is_even(num):
            print(num * num, end=" ")
        else:
            print(num, end=" ")


num_str = input("Your number: ")
try:
    number = int(num_str)
except ValueError:
    print("Invalid input, must be an integer")
else:
    print(check_is_even(number))
    print_nums(number)
