#!/usr/bin/python3
"""Defines the Message class."""

from models import db, app
from models.base import Base

class Message(Base, db.Model):
    """Defines the Message class and inherit from Base model."""
    __tablename__ ='messages'
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text(255), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    sender_id = db.Column(db.String(60), nullable=False)
    reciever_id = db.Column(db.String(60), nullable=False)
