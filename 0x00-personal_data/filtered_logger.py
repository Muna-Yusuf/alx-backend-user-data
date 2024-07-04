#!/usr/bin/env python3
"""Filtered logger"""

import logging
import re
from typing import List
import os
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ __init__ """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format """
        message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Replace sensitive fields in a log message with redacted text"""
    pattern = '|'.join(
        f'{field}=[^{separator}]*' for field in fields
    )
    return re.sub(
        pattern,
        lambda m: f"{m.group().split('=')[0]}={redaction}",
        message
    )


def get_logger() -> logging.Logger:
    """Create and configure logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the database"""
    db_connection = mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "localhost"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "root"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return db_connection


def main():
    """Main function to read and filter database data"""
    con = get_db()
    users = con.cursor()
    users.execute("SELECT CONCAT('name=', name, ';ssn=', ssn, ';ip=', ip, \
        ';user_agent', user_agent, ';') AS message FROM users;")
    formatter = RedactingFormatter(fields=PII_FIELDS)
    logger = get_logger()

    for user in users:
        logger.log(logging.INFO, user[0])


if __name__ == "__main__":
    main()
