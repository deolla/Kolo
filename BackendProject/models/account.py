#!/usr/bin/python3
"""Defines the User class."""
from models import db, app
from models.base import Base
from datetime import datetime
from models.user import User


class Account(Base, db.Model):
    """Defines the Account class and inherit from Base model."""

    __tablename__ = "accounts"
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    account_name = db.Column(db.String(60), nullable=False)
    account_number = db.Column(db.String(60), nullable=False)
    account_type = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.DateTime, default=datetime.utcnow)
    close_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, nullable=True)

    # Relationships
    user = db.relationship("User", backref="accounts", lazy=True)
