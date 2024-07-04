#!/usr/bin/env python3
"""Filtered logger"""

import logging
import re

def filter_datum(fields, redaction, message, separator):
    """Replace sensitive fields in a log message with redacted text"""
    pattern = '|'.join(
        f'{field}=[^{separator}]*' for field in fields
    )
    return re.sub(
        pattern,
        lambda m: f"{m.group().split('=')[0]}={redaction}",
        message
    )

