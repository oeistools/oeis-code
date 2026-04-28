# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A066096 - lower Wythoff sequence: floor(n*phi), where phi = (1 + sqrt(5))/2.
https://oeis.org/A066096
"""

from functools import lru_cache
from math import floor, sqrt
from typing import Literal

from ..backends import pari as pari_backend
from ..registry import register


@register("A066096")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th term of the lower Wythoff sequence.
    a(n) = floor(n * phi)
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return int(pari_backend.pari(f"({n} + sqrtint(5*{n}^2)) \\ 2"))

    phi = (1 + sqrt(5)) / 2
    return floor(n * phi)
