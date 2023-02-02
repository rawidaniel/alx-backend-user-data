#!/usr/bin/env python3
"""
Module encrypt_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Reterive a salted, hashed password, which is a byte string.
    Parameters
    ----------
    password: str
      password to be hashed
    """
    encode = password.encode()
    hashed = bcrypt.hashpw(encode, bcrypt.gensalt())
    return hashed
