
from typing import List

from ..utils.math import is_prime


def primes(n: int) -> List[int]:
    """
    Generate the first n prime numbers.

    Args:
        n: The number of primes to generate.

    Returns:
        A list of the first n prime numbers.
    """
    res: List[int] = []
    num = 2
    while len(res) < n:
        if is_prime(num):
            res.append(num)
        num += 1
    return res

def fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.

    Args:
        n: The number of Fibonacci terms to generate.

    Returns:
        A list of the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    res = [0]
    if n == 1:
        return res
    res.append(1)
    a, b = 0, 1
    while len(res) < n:
        a, b = b, a + b
        res.append(b)
    return res
