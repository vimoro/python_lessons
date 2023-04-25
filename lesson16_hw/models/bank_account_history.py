from datetime import datetime

from sqlalchemy import Enum as sqlalchemy_enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.operation import OperationEnum


class BankAccountHistory(Base):
    __tablename__ = "bankaccounthistory"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]
    operation: Mapped[str] = mapped_column(sqlalchemy_enum(OperationEnum))
    date_time: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    bank_account_id: Mapped[int] = mapped_column(ForeignKey('bankaccount.id'))
    bank_account: Mapped[list["BankAccount"]] = relationship(back_populates="_history")

    def __repr__(self):
        return f'BankAccountHistory({self.operation}-{self.amount})'
