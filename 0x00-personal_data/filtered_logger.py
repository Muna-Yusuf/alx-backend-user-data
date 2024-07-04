#!/usr/bin/env python3
"""Filtered logger"""

import logging
import re

def filter_datum(fields, redaction, message, separator):
    """Replace sensitive fields in a log message with redacted text"""
    return re.sub(r"(\w+)=([a-zA-Z0-9@\.\-\(\)\ \:\^\<\>\~\$\%\@\?\!\/]*)",
                  lambda match: match.group(1) + "=" + redaction
                  if match.group(1) in fields else match.group(0), message)
