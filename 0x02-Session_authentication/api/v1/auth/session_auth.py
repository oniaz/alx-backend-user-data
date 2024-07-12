#!/usr/bin/env python3
""" Session Auth module docs
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class docs"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create_session method docs"""
        if user_id is None or type(user_id) != str:
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
