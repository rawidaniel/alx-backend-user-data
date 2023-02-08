#!/usr/bin/env python3
"""
Module basic_auth
"""
from api.v1.auth.auth import Auth


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
