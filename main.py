from models import db, app
from models.base import *
from models.user import *
from models.transaction import *
from models.card import *
from models.account import *
from models.loan import *
from models.security import *
from flask import render_template



with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def splash_screen():
    """Display splash screen for the bank logo"""
    return render_template('splash.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)