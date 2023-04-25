from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.operation import OperationEnum
from models.bank_account_history import BankAccountHistory


class NotEnoughMoneyError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class BankAccount(Base):
    __tablename__ = "bankaccount"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    _balance: Mapped[int] = mapped_column("balance", nullable=False)
    _history: Mapped[list["BankAccountHistory"]] = relationship(back_populates="bank_account")

    def __repr__(self):
        return f'BankAccountHistory({self.name}: {self.balance})'

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        return self._history

    def replenish(self, amount: int):
        self._balance += amount
        self._history.append(
            BankAccountHistory(
                amount=amount,
                operation=OperationEnum.PLUS,
            )
        )

    def withdraw(self, amount: int):
        if self.balance < amount:
            raise NotEnoughMoneyError(f"You don't have enough money to withdraw {amount}")
        self._balance -= amount
        self._history.append(
            BankAccountHistory(
                amount=amount,
                operation=OperationEnum.MINUS,
            )
        )
