from flask import jsonify, request, Blueprint
from models.user import User
from models import db, app

user_routes = Blueprint('user_routes', __name__, url_prefix='/users')

@user_routes.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    users = User.query.all()
    return jsonify(users=[user.serialise() for user in users]), 200


@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get a single user."""
    user = User.query.filter_by(id=user_id).first()
    if user:
        return jsonify(user.serialise()), 200
    return jsonify({'message': 'User not found'}), 404


@user_routes.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialise()), 201

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if user:
        user.update(**data)
        db.session.commit()
        return jsonify(user.serialise()), 200
    return jsonify({'message': 'User not found'}), 404

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.filter_by(id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404

