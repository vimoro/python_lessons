import db
from models import Base
from models.bank_account import BankAccount, NotEnoughMoneyError


db.configure_engine()
Base.metadata.drop_all(db.engine)
Base.metadata.create_all(db.engine)

session = db.Session()

my_bank_account = BankAccount(name="Vika's account", _balance=0)
my_bank_account.replenish(500)
session.add(my_bank_account)
session.commit()

my_bank_account.withdraw(100)
session.commit()

print(my_bank_account.balance)
print(my_bank_account.history)

try:
    my_bank_account.withdraw(500)
except NotEnoughMoneyError as e:
    print(e)
