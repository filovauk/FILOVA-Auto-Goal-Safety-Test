"""Synthetic fixture for the auto-goal P-5 review test. No real project code."""


def add(a, b):
    """Return the sum of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add() takes two integers")
    return a + b
