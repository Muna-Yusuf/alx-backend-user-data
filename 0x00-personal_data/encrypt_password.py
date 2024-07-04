#!/usr/bin/env python3
"""
Password encryption
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password.
    """
    if password:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a hashed password
    """
    if hashed_password and password:
        return bcrypt.checkpw(password.encode(), hashed_password)
    return False  # Return False if either argument is None or empty
