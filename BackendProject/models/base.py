#!/usr/bin/python
"""Base class for all models"""

from datetime import datetime
from uuid import uuid4
from models import db
from flask_sqlalchemy import SQLAlchemy




class Base():
    """Base class for all models"""
    id = db.Column(db.String(60), primary_key=True, unique=True, default=str(uuid4()), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(cls):
        return f'<{type(cls)} {cls.id}>'