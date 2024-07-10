#!/usr/bin/env python3
""" basic auth module docs
"""

from api.v1.auth.auth import Auth
import base64


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
        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header method docs"""
        if (
            not base64_authorization_header or
            type(base64_authorization_header) != str
        ):
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials method docs"""
        if (
            not decoded_base64_authorization_header or
            type(decoded_base64_authorization_header) != str or
            ':' not in decoded_base64_authorization_header
        ):
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
