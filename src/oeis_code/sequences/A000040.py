# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A000040 - Prime numbers
https://oeis.org/A000040
"""

from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..backends import python as py_backend
from ..registry import register


@register("A000040")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th prime number.
    A000040: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return pari_backend.prime(n)
    return py_backend.n_th_prime(n)
