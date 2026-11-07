"""Synthetic fixture for the auto-goal P-5 review test. No real project code."""


def add(a, b):
    """Return the sum of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add() takes two integers")
    return a + b


def sub(a, b):
    """Return a minus b for two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("sub() takes two integers")
    return a - b


def mul(a, b):
    """Return a times b for two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("mul() takes two integers")
    return a * b
