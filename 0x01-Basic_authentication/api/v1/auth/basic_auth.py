#!/usr/bin/env python3
"""
Module basic_auth
"""
from api.v1.auth.auth import Auth
import base64
import binascii


class BasicAuth(Auth):
    """
    A class that represent BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract the Base64 part of the Authorization header
           for a Basic Authentication

        Parameters
        ----------
        authorization_header: str
            authorization header

        Returns
        ------
        str
            the Base64 part of the Authorization header
        """
        if authorization_header is None or type(authorization_header) != str:
            return
        if not authorization_header.startswith("Basic "):
            return
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Reterive the decoded value of a Base64 string
           base64_authorization_header

        Parameters
        ---------
        base64_authorization_header: str
            base64 authorization header

        Returns
        -------
        str:
            decoded value of a Base64 string
        """
        if base64_authorization_header is None\
           or type(base64_authorization_header) != str:
            return
        try:
            byte_result = base64.b64decode(base64_authorization_header)
            str_result = byte_result.decode("utf-8")
        except binascii.Error as e:
            return
        return str_result
