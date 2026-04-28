# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

from ..utils.math import fibonacci_term, is_prime


def n_th_prime(n: int) -> int:
    """
    Get the n-th prime number (1-indexed).

    Args:
        n: The index of the prime.

    Returns:
        The n-th prime number.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
    return num


def fibonacci(n: int) -> int:
    """
    Get the n-th Fibonacci number.

    Args:
        n: The index of the Fibonacci number.

    Returns:
        The n-th Fibonacci number.
    """
    return fibonacci_term(n)
