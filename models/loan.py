#!/usr/bin/python3
"""Defines the Loan class."""

from models import db, app
from models.base import Base

class Loan(Base, db.Model):
    """Defines the Loan class and inherit from Base model."""
    __tablename__ = 'loans'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    loan_type = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    loan_date = db.Column(db.DateTime, nullable=False)
    interest = db.Column(db.Float, nullable=False)
    term = db.Column(db.String(60), nullable=False) # loan duration in months
    status = db.Column(db.String(60), nullable=False) # approved, pending, or rejected.
