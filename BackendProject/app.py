import re
from models import app, db,  bcrypt
from models.user import User
from flask import request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import jwt



MAX_FAILED_ATTEMPTS = 3
LOCK_TIMEOUT = timedelta(minutes=30)


with app.app_context():
    db.create_all()

CORS(app)

@app.route('/', methods=['GET'])
def splash():
    return {'message': 'Welcome to Kolo!'}


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            response = {'message': 'Login successful'}
            return jsonify(response), 200
        else:
            response = {'message': 'Invalid credentials'}
            return jsonify(response), 401


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()

        email = data.get('email')
        fullname = data.get('fullname')
        username = data.get('username')
        phone = data.get('phone')
        password = data.get('password')
        address = data.get('address')

        # Perform validation
        errors = {}

        if not email or not re.match(r'\S+@\S+\.\S+', email):
            errors['email'] = 'Please enter a valid email address'

        if not fullname:
            errors['fullname'] = 'Please enter your fullname'

        if not username:
            errors['username'] = 'Please enter your username'
        elif User.query.filter_by(username=username).first():
            errors['username'] = 'Username already exists'

        if not phone:
            errors['phone'] = 'Please enter your phone number'

        if not password or len(password) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if not address:
            errors['address'] = 'Please enter your address'

        if errors:
            return jsonify({'errors': errors}), 400

        # Check for duplicate email
        if User.query.filter_by(email=email).first():
            return jsonify({'errors': {'email': 'Email already exists'}}), 400

        # Registration logic
        new_user = User(
            email=email,
            fullname=fullname,
            username=username,
            phone=phone,
            password=password,
            address=address
        )

        db.session.add(new_user)
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Registration successful'}), 200
    else:
        # Handle other HTTP methods if needed
        return jsonify({'message': 'Method not allowed'}), 405
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
