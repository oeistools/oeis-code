"""
A000045 - Fibonacci numbers
https://oeis.org/A000045
"""

from typing import List, Literal
from functools import lru_cache
from ..registry import register
from ..backends import pari as pari_backend
from ..backends import python as py_backend

@register("A000045")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> List[int]:
    """
    Generate the first n Fibonacci numbers.
    A000045: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return [pari_backend.fibonacci(i) for i in range(n)]
    return py_backend.fibonacci(n)
