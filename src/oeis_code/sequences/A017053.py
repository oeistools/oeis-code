"""
A017053 - a(n) = 7*n + 6.
https://oeis.org/A017053
"""

from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..registry import register


@register("A017053")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th term of the sequence a(n) = 7*n + 6.
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return int(pari_backend.pari(f"7*{n} + 6"))

    return 7 * n + 6
