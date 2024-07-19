#!/usr/bin/env python3
""" Auth Models."""

from bcrypt import hashpw, gensalt, checkpw
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes password and returns the salted hash in bytes."""
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed
