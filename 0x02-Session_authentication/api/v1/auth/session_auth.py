#!/usr/bin/env python3
""" Session Auth module docs
"""
from api.v1.auth.auth import Auth
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class SessionAuth(Auth):
    """SessionAuth class docs"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create_session method docs"""
        if user_id is None or type(user_id) != str:
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id
        return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method docs"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns a User instance based on a cookie value
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user
