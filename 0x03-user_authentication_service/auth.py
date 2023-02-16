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

    def valid_login(self, email: str, password: str) -> bool:
        """ Validate the login credential

        Parameters
        ---------
        email: str
            user email
        password: str
            user password

        Returns
        -------
        bool
            True if user provide valid credential or False
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode("utf-8"),
                                      user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Create session id

        Parameters
        ----------
        email: str
            user email

        Returns
        -------
        str
            session id or None
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            kwargs = {"session_id": session_id}
            self._db.update_user(user.id, **kwargs)
            return session_id
        except Exception:
            return

    def get_user_from_session_id(self, session_id: str) -> User:
        """Reterive user object based on provided session id

        Parameters
        ----------
        session_id: str
            session id stored for specific user

        Returns
        -------
        object
            user object or None
        """
        if session_id is None:
            return
        try:
            kwargs = {"session_id": session_id}
            user = self._db.find_user_by(**kwargs)
            return user
        except Exception:
            return

    def destroy_session(self, user_id: int) -> None:
        """Delete user's session id

        Parameters
        ----------
        user_id: int
            user id
        """
        self._db.update_user(user_id, session_id=None)
        return

    def get_reset_password_token(self, email: str) -> str:
        """Generate token

        Parameters
        ----------
        email: str
            user email

        Returns
        ------hashed_password = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_password, )
            token generated b _generte_uuid function
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            user = self._db.update_user(user.id, reset_token=token)
            return token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password

        Parameters
        ----------
        reset_token: str
            token id
        password: str
            user password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
