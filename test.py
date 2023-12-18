# Import your models
from models.account import Account
from models.transaction import Transaction
from models.card import Card
from models.user import User
from models import db, app
from uuid import uuid4
from datetime import datetime as DateTime

# Create a user


with app.app_context():
    # db.create_all()
    user = User(id=str(uuid4()), first_name="joe", last_name="Doe", password='hashed_password', phone=812345689, address='1234')
    
    account = Account(user_id=user.id, account_number='023456789', account_type='savings', account_name='Oluwaseyi Adeosun', email='deosundeola@gmail.com', balance=2000 )
    # transaction = Transaction(id=str(uuid4()), account_id=account.id, transaction_type='deposit', amount=500.00)
    # card = Card(id=str(uuid4()), card_type='visa', card_number='1234567890123456', cvv='123', card_pin='1234', expiration_date='2020-12-12')
    db.session.add(account)
    db.session.add(user)
    # db.session.add(transaction)
    # db.session.add(card) 
    db.session.commit()
    m = Account.query.all()
    print(m)
    # print(m[0].transactions)
    # print(Transaction.query.all())

    # i = Transaction.query.all()
    # print(i)
    # print(i[0].account)
    # print(Account.query.all())
    # print(User.query.all())
