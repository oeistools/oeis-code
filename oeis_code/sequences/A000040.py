
"""
A000040 - Prime numbers
https://oeis.org/A000040
"""

from oeis_code.registry import register
from oeis_code.backends import pari as pari_backend
from oeis_code.backends import python as py_backend

@register("A000040")
def sequence(n, backend="python"):
    if backend == "pari" and pari_backend.AVAILABLE:
        return [pari_backend.prime(i) for i in range(1, n+1)]
    return py_backend.primes(n)
