"""
A066096 - lower Wythoff sequence: floor(n*phi), where phi = (1 + sqrt(5))/2.
https://oeis.org/A066096
"""

from typing import List, Literal
from functools import lru_cache
from math import floor, sqrt
from ..registry import register
from ..backends import pari as pari_backend

@register("A066096")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> List[int]:
    """
    Generate the first n terms of the lower Wythoff sequence.
    a(n) = floor(n * phi)
    """
    if backend == "pari" and pari_backend.AVAILABLE:
        return [
            int(pari_backend.pari(f"({k} + sqrtint(5*{k}^2)) \\ 2"))
            for k in range(n)
        ]
    
    phi = (1 + sqrt(5)) / 2
    return [floor(k * phi) for k in range(n)]