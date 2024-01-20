from flask import jsonify, request, Blueprint
from models import db
from models.account import Account
from models.transaction import Transaction
from datetime import datetime

account_routes = Blueprint('account_route', __name__, url_prefix='/accounts')


@account_routes.route('/users/<user_id>/account_details', methods=['GET'])
def account_details(user_id):
    """Get account details for a user."""
    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    return jsonify({'account_details': account.serialize()}), 200

@account_routes.route('/users/<user_id>/account_balance', methods=['GET'])
def account_balance(user_id):
    """Get the account balance for a user."""
    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    return jsonify({'account_balance': account.balance}), 200

@account_routes.route('/users/<user_id>/transfer_funds', methods=['POST'])
def transfer_funds(user_id):
    """Transfer funds between accounts."""
    data = request.json
    recipient_account_number = data.get('recipient_account_number')
    amount = data.get('amount')
    description = data.get('description')

    sender_account = Account.query.filter_by(user_id=user_id).first()
    recipient_account = Account.query.filter_by(account_number=recipient_account_number).first()

    if not sender_account or not recipient_account:
        return jsonify({'error': 'Invalid sender or recipient account'}), 404

    # Ensure the sender has sufficient balance
    if sender_account.balance < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    # Perform the fund transfer
    sender_account.balance -= amount
    recipient_account.balance += amount

    # Record the transaction for both sender and recipient
    transaction_sender = Transaction(
        account_id=sender_account.id,
        transaction_type='transfer',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=description,
        status='completed'
    )
    transaction_recipient = Transaction(
        account_id=recipient_account.id,
        transaction_type='transfer',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=description,
        status='completed'
    )

    db.session.add_all([transaction_sender, transaction_recipient])
    db.session.commit()

    return jsonify({'message': 'Funds transferred successfully'}), 200

@account_routes.route('/users/<user_id>/transaction_history', methods=['GET'])
def transaction_history(user_id):
    """Get transaction history for a user."""
    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    transactions = Transaction.query.filter_by(account_id=account.id).all()

    return jsonify({'transactions': [transaction.serialize() for transaction in transactions]}), 200

@account_routes.route('/users/<user_id>/deposit', methods=['POST'])
def deposit(user_id):
    """Deposit funds into the account."""
    data = request.json
    amount = data.get('amount')
    description = data.get('description')

    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    # Perform the deposit
    account.balance += amount

    # Record the deposit transaction
    transaction = Transaction(
        account_id=account.id,
        transaction_type='deposit',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=description,
        status='completed'
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({'message': 'Deposit successful'}), 200

@account_routes.route('/users/<user_id>/withdraw', methods=['POST'])
def withdraw(user_id):
    """Withdraw funds from the account."""
    data = request.json
    amount = data.get('amount')
    description = data.get('description')

    account = Account.query.filter_by(user_id=user_id).first()

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    # Ensure the account has sufficient balance
    if account.balance < amount:
        return jsonify({'error': 'Insufficient funds'}), 400

    # Perform the withdrawal
    account.balance -= amount

    # Record the withdrawal transaction
    transaction = Transaction(
        account_id=account.id,
        transaction_type='withdrawal',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=description,
        status='completed'
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({'message': 'Withdrawal successful'}), 200

