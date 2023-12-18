#!/usr/bin/python3
"""Defines the Card class."""

from models import db, app
from models.base import Base

class Card(Base, db.Model):
    """Defines the Card class and inherit from Base model."""
    __tablename__ = 'cards'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    card_type = db.Column(db.String(60), nullable=False)
    card_number = db.Column(db.String(60), nullable=False)
    expiration_date = db.Column(db.String(60), nullable=False)
    card_pin = db.Column(db.String(60), nullable=False)
    cvv = db.Column(db.String(60), nullable=False)

    # Relationships
    # user = db.relationship('User', backref=db.backref('cards', lazy='dynamic'))