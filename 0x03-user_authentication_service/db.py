#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User
from typing import TypeVar, Dict
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

column = ["id",
          "email",
          "hashed_password",
          "session_id",
          "reset_token"]


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """create a user in the database

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
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find user based on given arbitrary argument

        Parameters
        ---------
        kwargs: dict
            arbitrary keyword arguments

        Returns
        -------
        object
            user object or raise error
        """
        for key in kwargs.keys():
            if key not in column:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """update user based on given arbitrary argument

        Parameters
        ---------
        user_id:int
            user id
        kwargs: dict
            arbitrary keyword arguments
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in column:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
        return
