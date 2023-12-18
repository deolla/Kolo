#!/usr/bin/python3
"""Defines the User class."""
from models import db, app
from models.base import *
from flask_bcrypt import Bcrypt
from models.loan import *
from models.card import *
from models.account import *
from models.security import *
from models.transaction import *
from models.message import *

class User(Base, db.Model):
    """Defines a User class and inherit from Base model."""
    __tablename__ = 'users'
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(60), nullable=True)
    is_active = db.Column(db.Boolean, nullable=True, default=True)


    # Relationships
    accounts = db.relationship('Account', backref='users', lazy=True)
    cards = db.relationship('Card', backref='users', lazy=True)
    loans = db.relationship('Loan', backref='users', lazy=True)
    messages = db.relationship('Message', backref='users', lazy=True)
    security_info = db.relationship('Security', backref='users', lazy=True)

    def set_password(self, password):
        """Set password."""
        self.password_hash = Bcrypt().generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check password."""
        return Bcrypt().check_password_hash(self.password_hash, password)
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True
    
    def is_active(self):
        """Return True if the user is active."""
        if self.is_active:
            return True
        return True    
    def get_id(self):
        """Return the id of the user."""
        return str(self.id)