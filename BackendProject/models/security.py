#!/usr/bin/python3
"""Defines the Security class."""

from models import db, app
from models.base import Base

class Security(Base, db.Model):
    """Defines the Security class and inherit from Base model."""
    __tablename__ ='securities'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    question_1 = db.Column(db.String(60), nullable=True)
    answer_1 = db.Column(db.String(60), nullable=True)
    question_2 = db.Column(db.String(60), nullable=True)
    answer_2 = db.Column(db.String(60), nullable=True)
    pin = db.Column(db.String(4), nullable=True)