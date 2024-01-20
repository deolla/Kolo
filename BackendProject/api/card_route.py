from models.user import User
from models.card import Card
from models.transaction import Transaction
from flask import jsonify, request, Blueprint
from datetime import datetime
from models import db

card_routes = Blueprint('card_route', __name__, url_prefix='/cards')


@card_routes.route('/users/<user_id>/add_card', methods=['POST'])
def add_card(user_id):
    """Add a new card for a user."""
    data = request.json
    card_type = data.get('card_type')
    card_number = data.get('card_number')
    expiration_date = data.get('expiration_date')
    card_pin = data.get('card_pin')
    cvv = data.get('cvv')

    # Check if the user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create and store the new card
    card = Card(
        user_id=user_id,
        card_type=card_type,
        card_number=card_number,
        expiration_date=expiration_date,
        card_pin=card_pin,
        cvv=cvv
    )

    db.session.add(card)
    db.session.commit()

    return jsonify({'message': 'Card added successfully', 'added_card': card.serialize()}), 200

@card_routes.route('/users/<user_id>/get_cards', methods=['GET'])
def get_cards(user_id):
    """Get the cards for a user."""
    cards = Card.query.filter_by(user_id=user_id).all()

    return jsonify({'cards': [card.serialize() for card in cards]}), 200

@card_routes.route('/users/<user_id>/delete_card/<card_id>', methods=['DELETE'])
def delete_card(user_id, card_id):
    """Delete a card."""
    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    db.session.delete(card)
    db.session.commit()

    return jsonify({'message': 'Card deleted successfully'}), 200

@card_routes.route('/users/<user_id>/update_card/<card_id>', methods=['PUT'])
def update_card(user_id, card_id):
    """Update card details."""
    data = request.json
    card_type = data.get('card_type')
    expiration_date = data.get('expiration_date')
    cvv = data.get('cvv')

    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    card.card_type = card_type
    card.expiration_date = expiration_date
    card.cvv = cvv

    db.session.commit()

    return jsonify({'message': 'Card details updated successfully', 'updated_card': card.serialize()}), 200

@card_routes.route('/users/<user_id>/make_transaction/<card_id>', methods=['POST'])
def make_transaction(user_id, card_id):
    """Make a transaction using a card."""
    data = request.json
    amount = data.get('amount')
    description = data.get('description')

    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    # Create and store the transaction
    transaction = Transaction(
        account_id=card.user.accounts[0].id,  # Assuming the user has at least one account
        transaction_type='debit',
        amount=amount,
        transaction_date=datetime.utcnow(),
        description=description,
        status='completed'
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({'message': 'Transaction completed successfully', 'transaction': transaction.serialize()}), 200


@card_routes.route('/users/<user_id>/card_transactions/<card_id>', methods=['GET'])
def card_transactions(user_id, card_id):
    """Get transaction history for a card."""
    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    transactions = Transaction.query.filter_by(account_id=card.user.accounts[0].id).all()

    return jsonify({'transactions': [transaction.serialize() for transaction in transactions]}), 200

@card_routes.route('/users/<user_id>/block_card/<card_id>', methods=['PUT'])
def block_card(user_id, card_id):
    """Block a card."""
    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    card.is_blocked = True
    db.session.commit()

    return jsonify({'message': 'Card blocked successfully', 'blocked_card': card.serialize()}), 200

@card_routes.route('/users/<user_id>/unblock_card/<card_id>', methods=['PUT'])
def unblock_card(user_id, card_id):
    """Unblock a card."""
    card = Card.query.get(card_id)

    if not card or card.user_id != user_id:
        return jsonify({'error': 'Invalid card or user'}), 404

    card.is_blocked = False
    db.session.commit()

    return jsonify({'message': 'Card unblocked successfully', 'unblocked_card': card.serialize()}), 200


