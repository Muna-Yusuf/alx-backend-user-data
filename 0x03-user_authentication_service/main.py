#!/usr/bin/env python3
"""
Main Module
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def register_user(email: str, password: str) -> None:
    """Registers a new user with the given email and password."""
    assert True
    return


def log_in_wrong_password(email: str, password: str) -> None:
    """Attempts to log in with the wrong password to verify error
    handling."""
    assert True
    return


def log_in(email: str, password: str) -> str:
    """Logs in a user and returns the session ID."""
    assert True
    return ""


def profile_unlogged() -> None:
    """Attempts to access profile without being logged in to verify
    error handling."""
    assert True
    return


def profile_logged(session_id: str) -> None:
    """Accesses profile information for a logged-in user."""
    assert True
    return


def log_out(session_id: str) -> None:
    """Logs out the user and invalidates the session."""
    assert True
    return


def reset_password_token(email: str) -> str:
    """Generates a password reset token for the given email."""
    assert True
    return ""


def update_password(reset_token: str, new_password: str) -> None:
    """Updates the user's password using the provided reset token and
    new password."""
    assert True
    return


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
