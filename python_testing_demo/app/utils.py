import re
from typing import Iterable, List

_slug_re = re.compile(r"[^a-z0-9]+")


def is_strong_password(p: str, min_len: int = 8) -> bool:
    """
    Very simple strength check: length, upper, lower, digit, special.
    """
    if not isinstance(p, str):
        return False
    if len(p) < min_len:
        return False
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    has_special = any(not c.isalnum() for c in p)
    return all([has_upper, has_lower, has_digit, has_special])

def mean(values: Iterable[float]) -> float:
    """
    Compute arithmetic mean. Raises ValueError on empty input.
    """
    vals: List[float] = list(values)
    if not vals:
        raise ValueError("values must not be empty")
    return sum(vals) / len(vals)

def fibonacci(n: int) -> int:
    """
    Iterative fibonacci for non-negative n.
    """
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
