#!/usr/bin/env python3
"""
Module filtered_logger
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Reterive the log message obfuscated
    Parameters
    ----------
    fields: list
        a list of strings representing all fields to obfuscate
    redaction: str
        a string representing by what the field will be obfuscated
    message: str
        a string representing the log line
    separator: str
        a string representing by which character is separating
        all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
