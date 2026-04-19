

try:
    from cypari2 import Pari
    pari = Pari()
    AVAILABLE = True
except ImportError:
    AVAILABLE = False

def prime(n: int) -> int:
    """Get the n-th prime number using PARI/GP."""
    return int(pari(f"prime({n})"))

def fibonacci(n: int) -> int:
    """Get the n-th Fibonacci number using PARI/GP."""
    return int(pari(f"fibonacci({n})"))
