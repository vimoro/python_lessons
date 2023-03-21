# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

from datetime import datetime


def log_info(func):
    def inner(*args, **kwargs):
        time = datetime.now()
        result = func(*args, **kwargs)
        log_message = f'Функция add вызвана в {time}'
        additional_info = []
        if args:
            additional_info.append(f'с позиционными параметрами {args}')
        if kwargs:
            additional_info.append(f'с именнованными параметрами {kwargs}')
        if additional_info:
            log_message += ' ' + ' и '.join(additional_info)
        else:
            log_message += ' без параметров'
        print(log_message)
        return result
    return inner


@log_info
def add(a=0, b=0):
    return a + b


add(1, 2)
add(a=1, b=2)
add(1, b=2)
add()
