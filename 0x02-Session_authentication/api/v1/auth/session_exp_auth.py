#!/usr/bin/env python3
"""
Module session_exp_auth
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
import uuid
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    A class that represent a session expiration time
    """
    def __init__(self) -> None:
        """Initialize object of SesionExpAuth
        """
        self.session_duration = int(getenv("SESSION_DURATION", "0"))

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id with expire time

        Parameters
        ----------
        user_id: str
            user id

        Returns
        -------
        str
          A session id for user id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return
        session_dictionary = {}
        session_dictionary["user_id"] = user_id
        session_dictionary["created_at"] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Reterive a User ID based on a Session ID:

        Parameters
        ---------
        session_id: str
          A session id

        Returns
        -------
        str
            A user id
        """
        if session_id is None:
            return
        if session_id not in self.user_id_by_session_id.keys():
            return
        session_dictionary = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")
        if "created_at" not in session_dictionary.keys():
            return
        if session_dictionary.get("created_at")\
           + timedelta(seconds=self.session_duration) < datetime.now():
            return
        return session_dictionary.get("user_id")
