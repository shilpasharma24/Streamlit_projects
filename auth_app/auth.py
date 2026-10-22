
import re
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password


def validate_username(username):
    return len(username) >= 3


def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_password(password):
    return len(password) >= 8
