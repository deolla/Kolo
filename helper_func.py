#!/usr/bin/python3
"""Helper functions"""

import secrets
import os

def get_secret_key():
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        secret_key = secrets.token_hex(16)
    return secret_key