from flask import jsonify, request, Blueprint
from models.security import Security
from models import db, app
from models.user import User
from datetime import datetime, timedelta
from helper_func import generate_reset_token, send_reset_email
from flask_jwt_extended import create_access_token
import pyotp

security_routes = Blueprint('security_routes', __name__, url_prefix='/security')


MAX_FAILED_ATTEMPTS = 3
LOCK_TIMEOUT = timedelta(minutes=30)# 24 hours

# MAX_SECURITY_ROUTES = 100

@security_routes.route('/users/request_password_reset', methods=['POST'])
def request_password_reset():
    """Request a password reset."""
    data = request.get_json()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found.'}), 404
    
    reset_token = generate_reset_token()
    user.reset_token = reset_token
    db.session.commit()

    send_reset_email(user.email, reset_token)

    return jsonify({'message': 'Password reset email sent.'}), 200

@security_routes.route('/users/reset_password/<reset_token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('new_password')
    
    user = User.query.filter_by(reset_token=token).first()
    if not user:
        return jsonify({'message': 'Invalid reset token.'}), 404
    
    user.set_password(new_password)
    user.reset_token = None
    db.session.commit()
    
    return jsonify({'message': 'Password reset.'}), 200

@security_routes.route('/users/login', methods=['POST'])
def login():
    """Authenticate the user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    
    if user and user.locked_until and user.locked_until > datetime.utcnow():
        return jsonify({'message': 'Account locked.'}), 403
    
    if not user or not user.check_password(password):
        if user:
            user.failed_attempts += 1
            if user.failed_attempts >= MAX_FAILED_ATTEMPTS:
                user.locked_until = datetime.utcnow() + LOCK_TIMEOUT
        db.session.commit()
        return jsonify({'message': 'Invalid credentials.'}), 401
    
    user.failed_attempts = 0
    user.locked_until = None
    db.session.commit()

    token = create_access_token(identity=user.id, expires_delta=False)
    log_message = f"Successful login for user {user.username}."
    app.logger.info(log_message)
    return jsonify({'message': 'Login successful.', 'token': token}), 200


@security_routes.route('/users/logout', methods=['POST'])
def logout():
    """Log the user out."""
    data = request.get_json()
    username = data.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Invalid username.'}), 404
    log_message = f"Successful logout for user {user.username}."
    app.logger.info(log_message)
    return jsonify({'message': 'Logout successful.'}), 200

@security_routes.route('/users/<user_id>/set_security_questions', methods=['POST'])
def set_security_questions(user_id):
    """Set security questions for a user."""
    data = request.json
    question_1 = data.get('question_1')
    answer_1 = data.get('answer_1')
    question_2 = data.get('question_2')
    answer_2 = data.get('answer_2')

    security = Security.query.filter_by(user_id=user_id).first()
    if not security:
        security = Security(user_id=user_id)

    # Set security questions and answers
    security.question_1 = question_1
    security.answer_1 = answer_1
    security.question_2 = question_2
    security.answer_2 = answer_2

    db.session.add(security)
    db.session.commit()

    return jsonify({'message': 'Security questions set successfully', 'security': security.serialize()}), 200

@security_routes.route('/users/<user_id>/set_pin', methods=['POST'])
def set_pin(user_id):
    """Set PIN for a user."""
    data = request.json
    pin = data.get('pin')

    security = Security.query.filter_by(user_id=user_id).first()
    if not security:
        security = Security(user_id=user_id)

    # Set PIN
    security.pin = pin

    db.session.add(security)
    db.session.commit()

    return jsonify({'message': 'PIN set successfully', 'security': security.serialize()}), 200



@security_routes.route('/users/<user_id>/enable_2fa', methods=['POST'])
def enable_2fa(user_id):
    """Enable 2FA for a user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Check if the user already has 2FA enabled
    security = Security.query.filter_by(user_id=user_id).first()
    if security and security.totp_secret:
        return jsonify({'message': '2FA is already enabled for this user'}), 400

    # Generate a new secret key for 2FA
    totp = pyotp.TOTP(pyotp.random_base32())
    secret_key = totp.secret

    # Store the secret key in the security model
    if not security:
        security = Security(user_id=user_id)
    
    security.totp_secret = secret_key
    db.session.commit()

    return jsonify({'message': '2FA enabled successfully', 'secret_key': secret_key}), 200

