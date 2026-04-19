
"""
A000045 - Fibonacci numbers
https://oeis.org/A000045
"""

from oeis_code.registry import register
from oeis_code.backends import pari as pari_backend
from oeis_code.backends import python as py_backend

@register("A000045")
def sequence(n, backend="python"):
    if backend == "pari" and pari_backend.AVAILABLE:
        return [pari_backend.fibonacci(i) for i in range(n)]
    return py_backend.fibonacci(n)
