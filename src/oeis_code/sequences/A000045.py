# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A000045 - Fibonacci numbers
https://oeis.org/A000045
"""

from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..backends import python as py_backend
from ..registry import register


@register("A000045")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th Fibonacci number.
    A000045: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return pari_backend.fibonacci(n)
    return py_backend.fibonacci(n)
