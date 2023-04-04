# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class OperationEnum(Enum):
    PLUS = 'incoming'
    MINUS = 'withdrawal'


@dataclass
class BankAccountHistory:
    amount: int
    operation: OperationEnum
    date_time: datetime


class NotEnoughMoneyError(Exception):
    pass


@dataclass
class BankAccount:
    # def __init__(self):
    #     self._balance = 0
    #     self._history = list()

    _balance: int = field(init=False, default=0)
    _history: list[BankAccountHistory] = field(init=False, default_factory=list)

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        return self._history

    def replenish(self, amount: int):
        self._balance += amount
        self._history.append(BankAccountHistory(amount, OperationEnum.PLUS, datetime.now()))

    def withdraw(self, amount: int):
        if self.balance < amount:
            raise NotEnoughMoneyError
        self._balance -= amount
        self._history.append(BankAccountHistory(amount, OperationEnum.MINUS, datetime.now()))


my_account = BankAccount()
print(f"{my_account.balance=}")
my_account.replenish(200)
print(f"{my_account.balance=}")
try:
    my_account.withdraw(50)
except NotEnoughMoneyError:
    print('недостаточно средст, чтобы совершить операцию')
else:
    print('сняли 50')
finally:
    print(f"{my_account.balance=}")

try:
    my_account.withdraw(250)
except NotEnoughMoneyError:
    print('недостаточно средст, чтобы совершить операцию')
else:
    print('сняли 250')
finally:
    print(f"{my_account.balance=}")

for history_record in my_account.history:
    if history_record.operation == OperationEnum.PLUS:
        print(history_record)


ann_account = BankAccount()
print(f"{ann_account.balance=}, {my_account.balance=}")
