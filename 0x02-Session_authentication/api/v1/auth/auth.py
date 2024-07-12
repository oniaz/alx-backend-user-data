#!/usr/bin/env python3
""" auth module docs
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class docs
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth fucntion docs
        """
        if not path or not excluded_paths:
            return True
        path = path if path.endswith('/') else path + '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ authorization_header fucntion docs
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user fucntion docs
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
