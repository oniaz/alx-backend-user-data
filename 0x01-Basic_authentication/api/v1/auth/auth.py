#!/usr/bin/env python3
""" auth module docs
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user fucntion docs
        """
        return None
