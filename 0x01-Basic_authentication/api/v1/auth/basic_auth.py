#!/usr/bin/env python3
""" basic auth module docs
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ basic auth class docs"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header method docs"""
        if (
            not authorization_header or
            type(authorization_header) != str or
            not authorization_header.startswith('Basic ')
        ):
            return None
        return authorization_header.removeprefix('Basic ')
