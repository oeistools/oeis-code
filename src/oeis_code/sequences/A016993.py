# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A016993 - a(n) = 7*n + 1.
https://oeis.org/A016993
"""

from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..registry import register


@register("A016993")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th term of the sequence a(n) = 7*n + 1.
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return int(pari_backend.pari(f"7*{n} + 1"))

    return 7 * n + 1
