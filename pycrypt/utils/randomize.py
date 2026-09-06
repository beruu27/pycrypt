"""Utilities for secure randomization."""
import secrets


def secure_token(n=16):
    return secrets.token_urlsafe(n)


def secure_bytes(n=32):
    return secrets.token_bytes(n)
