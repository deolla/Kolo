#!/usr/bin/python3
"""Helper functions"""

import secrets
import os
from flask_mail import Message
from flask import jsonify, current_app


def get_secret_key():
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        secret_key = secrets.token_hex(16)
    return secret_key

def generate_reset_token():
    """Generate a unique reset token."""
    # Use a secure method to generate a token (e.g., secrets module)
    reset_token = secrets.token_urlsafe(32)
    return reset_token

def send_reset_email(email, reset_token):
    from models import mail
    """Send the password reset email."""
    # Assuming you've initialized Flask-Mail and app.config.from_object('config') in __init__.py
    # Include the reset link in the email
    reset_link = f"{current_app.config['FRONTEND_URL']}/reset_password/{reset_token}"
    subject = "Password Reset Request"
    body = f"Click the following link to reset your password: {reset_link}"

    # Create a Flask-Mail message
    message = Message(subject, recipients=[email], body=body)

    # Send the email
    try:
        mail.send(message)
        return jsonify({'message': 'Password reset email sent successfully'}), 200
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({'error': 'Failed to send password reset email'}), 500