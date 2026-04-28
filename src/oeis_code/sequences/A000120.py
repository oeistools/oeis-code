"""
A000120 - 1's-counting sequence: number of 1's in binary expansion of n.
https://oeis.org/A000120
"""

from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..registry import register


@register("A000120")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th term of the 1's-counting sequence (Hamming weight of n).
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return int(pari_backend.pari(f"norml2(binary({n}))"))

    # Use n.bit_count() available in Python 3.10+
    if hasattr(n, "bit_count"):
        return n.bit_count()
    return bin(n).count("1")
