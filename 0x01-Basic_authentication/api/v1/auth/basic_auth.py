#!/usr/bin/env python3
""" basic auth module docs
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials method docs"""
        if (
            not user_email or type(user_email) != str or
            not user_pwd or type(user_pwd) != str
        ):
            return None
        try:
            users = User.search({'email': user_email})
            if not users or not users[0].is_valid_password(user_pwd):
                return None
        except Exception:
            return None

        return users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method docs """
        auth_header = self.authorization_header(request)
        b64_auth_header = self.extract_base64_authorization_header(
            auth_header
        )
        decoded_b64_auth = self.decode_base64_authorization_header(
            b64_auth_header
        )
        email, pwd = self.extract_user_credentials(
            decoded_b64_auth
        )
        return self.user_object_from_credentials(email, pwd)
