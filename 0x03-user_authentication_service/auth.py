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
