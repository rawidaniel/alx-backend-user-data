#!/usr/bin/env python3
"""
Module session_auth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    A class that represent Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id

        Parameters
        ----------
        user_id: str
            user id

        Returns
        -------
        str
          A session id for user id
        """
        if user_id is None or type(user_id) != str:
            return
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
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
        if session_id is None or type(session_id) != str:
            return
        return self.user_id_by_session_id.get(session_id)
