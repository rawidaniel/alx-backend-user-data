#!/usr/bin/env python3
"""
Module session_auth
"""
from api.v1.auth.auth import Auth
from models.user import User
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

    def current_user(self, request=None):
        """Reterive user object

        Parameters
        ----------
        request: object
            request object found when http request is sent

        Returns
        -------
        object
            user object
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user
