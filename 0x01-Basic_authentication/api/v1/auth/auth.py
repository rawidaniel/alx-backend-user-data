#!/usr/bin/env python3
"""
Module auth

"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class that represent Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Define which route don't need authentication

        Parameters
        ----------
        path: str
            endpoint to accessa resourec in Rest API
        Returns
        ------
        bool
            True if path not in excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization
        """
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """current user
        """
        return
