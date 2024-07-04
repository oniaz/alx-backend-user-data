#!/usr/bin/env python3
"""0x00. Personal data"""

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with a list of fields to redact
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and redact specified fields from the message
        """
        return filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        replacement = f"{field}={redaction}{separator}"
        message = re.sub(f"{field}=.*?{separator}", replacement, message)
    return message
