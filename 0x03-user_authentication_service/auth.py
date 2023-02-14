#!/usr/bin/env python3
"""
Module auth
"""
import bcrypt
from db import DB
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _generate_uuid() -> str:
    """Generate random number of id
    """
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Reterive hashed password

    Parameters
    ----------
    password: str
        user password

    Returns
    -------
    bytes
        salted hash of the input password
    """
    byte_password = password.encode("utf-8")
    hashed = bcrypt.hashpw(byte_password, bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register user into database

        Parameters
        ---------
        email: str
            user email
        hashed_password: str
            user hashed or hidden password

        Returns
        -------
        object
            user object
        """
        try:
            old_user = self._db.find_user_by(email=email)
            if old_user:
                raise ValueError(f"User {old_user.email} already exists")
        except NoResultFound:
            hased_password = _hash_password(password)
            user = self._db.add_user(email, hased_password)
        return user