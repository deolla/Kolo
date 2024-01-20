from flask import jsonify, request, Blueprint
from models.transaction import Transaction
from models import db
from models.account import Account
from datetime import datetime

transaction_routes = Blueprint('transaction_routes', __name__, url_prefix='/transactions')

@transaction_routes.route('/transactions', methods=['GET'])
def get_transactions():
    """Get all transactions."""
    transactions = Transaction.query.all()
    return jsonify(transactions=[transaction.serialise() for transaction in transactions]), 200

@transaction_routes.route('/transactions/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    """Get a single transaction."""
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    if transaction:
        return jsonify(transaction.serialise()), 200
    return jsonify({'message': 'Transaction not found'}), 404

@transaction_routes.route('/transactions', methods=['POST'])
def create_transaction():
    """Create a new transaction."""
    data = request.get_json()
    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(new_transaction.serialise()), 201

@transaction_routes.route('/transactions/<transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    """Update an existing transaction."""
    data = request.get_json()
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    if transaction:
        transaction.update(**data)
        db.session.commit()
        return jsonify(transaction.serialise()), 200
    return jsonify({'message': 'Transaction not found'}), 404

@transaction_routes.route('/transactions/<transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    """Delete a transaction."""
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return jsonify({'message': 'Transaction deleted'}), 200
    return jsonify({'message': 'Transaction not found'}), 404

@transaction_routes.route('/transactions/<transaction_id>/confirm', methods=['PUT', 'POST'])
def confirm_transaction(transaction_id):
    """Confirm a transaction."""
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    if transaction:
        transaction.confirm()
        db.session.commit()
        return jsonify(transaction.serialise()), 200
    return jsonify({'message': 'Transaction not found'}), 404

@transaction_routes.route('/transactions/<transaction_id>/cancel', methods=['PUT', 'POST'])
def cancel_transaction(transaction_id):
    """Cancel a transaction."""
    transaction = Transaction.query.filter_by(id=transaction_id).first()
    if transaction:
        transaction.cancel()
        db.session.commit()
        return jsonify(transaction.serialise()), 200
    return jsonify({'message': 'Transaction not found'}), 404

@transaction_routes.route('/transactions/transfers', methods=['POST'])
def transfer_funds():
    """Transfers funds between accounts."""
    data = request.get_json()
    sender_account = data.get('sender_account')
    reciever_account = data.get('reciever_account')
    amount = data.get('amount')

    if not sender_account.id or not reciever_account.id or not amount:
        return jsonify({'message': 'Invalid data'}), 400
    
    sender_account = Account.query.filter_by(id=sender_account.id).first()
    reciever_account = Account.query.filter_by(id=reciever_account.id).first()

    if not sender_account or not reciever_account:
        return jsonify({'message': 'Account not found'}), 404
    
    if sender_account.balance < amount:
        return jsonify({'message': 'Insufficient funds'}), 400
    
    sender_account.balance -= amount
    reciever_account.balance += amount

    new_transaction = Transaction(
        account_id=reciever_account.id,
        transaction_type='transfer',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=f'Transfer of {amount} from {sender_account.account_name} to {reciever_account.account_name}',
        status='completed'
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Funds transferred'}), 200



