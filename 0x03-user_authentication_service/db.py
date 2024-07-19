#!/usr/bin/env python3
"""
BD class
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


# List of valid attributes for user data
VALID_ATTRIBUTES = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']


class DB:
    """Database class"""

    def __init__(self):
        """Initialize the database connection and create tables."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Return a session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database.

        Args:
            email (str): User's email address.
            hashed_password (str): User's hashed password.

        Returns:
            User: The created User object.
        """
        if not email or not hashed_password:
            raise ValueError("Email and hashed_password cannot be empty.")
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by given arguments.

        Args:
            **kwargs: Filter criteria.

        Returns:
            User: The found User object.

        Raises:
            NoResultFound: If no user is found.
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound("No user found with the given criteria.")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attributes.

        Args:
            user_id (int): ID of the user to update.
            **kwargs: Attributes to update.

        Raises:
            ValueError: If an invalid attribute is provided.
        """
        user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if key not in VALID_ATTRIBUTES:
                raise ValueError(f"Invalid attribute: {key}.")
            setattr(user, key, val)
        self._session.commit()
