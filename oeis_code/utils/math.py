import math


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division.

    Args:
        n: The number to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Trial division up to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def fibonacci_term(n: int) -> int:
    """
    Calculate the n-th Fibonacci number (0-indexed).
    A000045: 0, 1, 1, 2, 3, 5, ...

    Args:
        n: The index of the term.

    Returns:
        The n-th Fibonacci number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
