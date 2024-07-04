#!/usr/bin/env python3
"""0x00. Personal data"""

from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        replacement = f"{field}={redaction}{separator}"
        message = re.sub(f"{field}=.*?{separator}", replacement, message)
    return message
