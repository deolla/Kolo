from flask import jsonify, request, Blueprint
from models.message import Message
from models.user import User
from models import db
from datetime import datetime

message_routes = Blueprint('message_routes', __name__, url_prefix='/messages')

@message_routes.route('/users/<user_id>/send_message', methods=['POST'])
def send_message(user_id):
    """Send a message to a user."""
    data = request.json
    content = data.get('content')
    subject = data.get('subject')
    sender_id = data.get('sender_id')

    # Check if the sender and receiver are valid users
    sender = User.query.get(sender_id)
    receiver = User.query.get(user_id)

    if not sender or not receiver:
        return jsonify({'error': 'Invalid sender or receiver'}), 404

    # Create and store the message
    message = Message(
        user_id=user_id,
        content=content,
        timestamp=datetime.utcnow(),
        subject=subject,
        sender_id=sender_id,
        receiver_id=user_id
    )

    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'Message sent successfully', 'sent_message': message.serialize()}), 200

@message_routes.route('/users/<user_id>/get_messages', methods=['GET'])
def get_messages(user_id):
    """Get messages for a user."""
    messages = Message.query.filter_by(user_id=user_id).all()

    return jsonify({'messages': [message.serialize() for message in messages]}), 200


@message_routes.route('/users/<user_id>/mark_as_read/<message_id>', methods=['PUT'])
def mark_message_as_read(user_id, message_id):
    """Mark a message as read."""
    message = Message.query.get(message_id)

    if not message or message.user_id != user_id:
        return jsonify({'error': 'Invalid message or user'}), 404

    message.read = True
    db.session.commit()

    return jsonify({'message': 'Message marked as read', 'marked_message': message.serialize()}), 200

@message_routes.route('/users/<user_id>/mark_as_unread/<message_id>', methods=['PUT'])
def mark_message_as_unread(user_id, message_id):
    """Mark a message as unread."""
    message = Message.query.get(message_id)

    if not message or message.user_id != user_id:
        return jsonify({'error': 'Invalid message or user'}), 404

    message.read = False
    db.session.commit()

    return jsonify({'message': 'Message marked as unread', 'marked_message': message.serialize()}), 200

@message_routes.route('/users/<user_id>/delete_message/<message_id>', methods=['DELETE'])
def delete_message(user_id, message_id):
    """Delete a message."""
    message = Message.query.get(message_id)

    if not message or message.user_id != user_id:
        return jsonify({'error': 'Invalid message or user'}), 404

    db.session.delete(message)
    db.session.commit()

    return jsonify({'message': 'Message deleted'}), 200



