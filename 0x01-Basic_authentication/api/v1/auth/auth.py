#!/usr/bin/env python3
""" auth module docs
"""
from flask import request


class Auth():
    """ Auth class docs
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth fucntion docs
        """
        return False
