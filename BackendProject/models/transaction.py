#!/usr/bin/python3
"""Defines the Transaction class."""

from models import db, app
from models.base import Base


class Transaction(Base, db.Model):
    """Defines the Transaction class and inherit from Base model."""

    __tablename__ = "transactions"
    account_id = db.Column(db.String(60), db.ForeignKey("accounts.id"), nullable=False)
    transaction_type = db.Column(
        db.String(60), nullable=False
    )  # deposit, withdraw, refund, refund or transfer.
    amount = db.Column(db.Integer, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(60), nullable=True)
    status = db.Column(
        db.String(60), nullable=False
    )  # Completed or pending transaction.

    accounts = db.relationship("Account", backref="transactions")
