# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""PARI/GP backend: computes terms through cypari2 when it can be imported."""

try:
    from cypari2 import Pari  # type: ignore

    pari = Pari()
    AVAILABLE = True
except (ImportError, ModuleNotFoundError):
    pari = None
    AVAILABLE = False


def _check_available() -> None:
    """Raise ImportError if the PARI/GP backend is not available."""
    if not AVAILABLE:
        raise ImportError(
            "The PARI/GP backend is not available. "
            "Please install 'cypari2' (pip install cypari2). "
            "Note: This may require PARI/GP development headers (e.g., libpari-dev)."
        )


def prime(n: int) -> int:
    """Get the n-th prime number using PARI/GP."""
    _check_available()
    return int(pari(f"prime({n})"))  # type: ignore


def fibonacci(n: int) -> int:
    """Get the n-th Fibonacci number using PARI/GP."""
    _check_available()
    return int(pari(f"fibonacci({n})"))  # type: ignore
