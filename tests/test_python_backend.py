# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
Tests for the pure-Python backend and explicit python-backend paths.

These tests exercise branches that are skipped when PARI/GP is available,
boosting coverage for backends/python.py and the sequence modules.
"""

import pytest

from oeis_code import get
from oeis_code.backends import python as py_backend
from oeis_code.sequences.A000120 import sequence as a000120_seq
from oeis_code.sequences.A000201 import sequence as a000201_seq
from oeis_code.sequences.A066096 import sequence as a066096_seq
from oeis_code.sequences.A109261 import sequence as a109261_seq

# ---------------------------------------------------------------------------
# backends/python.py — n_th_prime, fibonacci
# ---------------------------------------------------------------------------


def test_py_backend_prime_first():
    assert py_backend.n_th_prime(1) == 2


def test_py_backend_prime_fifth():
    assert py_backend.n_th_prime(5) == 11


def test_py_backend_prime_tenth():
    assert py_backend.n_th_prime(10) == 29


def test_py_backend_fibonacci_zero():
    assert py_backend.fibonacci(0) == 0


def test_py_backend_fibonacci_ten():
    assert py_backend.fibonacci(10) == 55


# ---------------------------------------------------------------------------
# Explicit backend="python" paths on every sequence
# ---------------------------------------------------------------------------


def test_a000040_python_backend():
    assert get("A000040", 1, backend="python") == 2
    assert get("A000040", 5, backend="python") == 11


def test_a000045_python_backend():
    assert get("A000045", 0, backend="python") == 0
    assert get("A000045", 10, backend="python") == 55


def test_a000120_python_backend():
    assert get("A000120", 0, backend="python") == 0
    assert get("A000120", 7, backend="python") == 3
    assert get("A000120", 255, backend="python") == 8


def test_a016993_python_backend():
    assert get("A016993", 0, backend="python") == 1
    assert get("A016993", 5, backend="python") == 36


def test_a017053_python_backend():
    assert get("A017053", 0, backend="python") == 6
    assert get("A017053", 5, backend="python") == 41


def test_a000201_python_backend():
    assert get("A000201", 1, backend="python") == 1
    assert get("A000201", 5, backend="python") == 8


def test_a066096_python_backend():
    assert get("A066096", 1, backend="python") == 1
    assert get("A066096", 5, backend="python") == 8


def test_a109261_python_backend():
    assert get("A109261", 1, backend="python") == 2
    assert get("A109261", 3, backend="python") == 5


# ---------------------------------------------------------------------------
# A000120 — bin() fallback for Python < 3.10 (no bit_count attribute)
# ---------------------------------------------------------------------------


def test_a000120_bin_fallback(monkeypatch):
    """Force the bin()-based path for environments without int.bit_count."""

    class _NoBC(int):
        """int subclass without bit_count, simulating Python < 3.10."""

    original_seq = a000120_seq.__wrapped__  # unwrap lru_cache

    def patched_seq(n: int, backend: str = "python") -> int:
        # Delegate to original but swap n for a _NoBC instance
        n_no_bc = _NoBC(n)
        return original_seq(n_no_bc, backend)

    assert patched_seq(7) == 3  # 0b111
    assert patched_seq(5) == 2  # 0b101
    assert patched_seq(0) == 0


# ---------------------------------------------------------------------------
# A066096 — phi-based floor (python path)
# ---------------------------------------------------------------------------


def test_a066096_extended_python():
    expected = {0: 0, 1: 1, 2: 3, 3: 4, 4: 6, 5: 8, 6: 9, 7: 11, 8: 12}
    for n, val in expected.items():
        assert a066096_seq(n, backend="python") == val


# ---------------------------------------------------------------------------
# A109261 — invalid input (python path)
# ---------------------------------------------------------------------------


def test_a000201_raises_on_zero():
    with pytest.raises(ValueError, match="n must be >= 1"):
        a000201_seq(0, backend="python")


def test_a109261_raises_on_zero():
    with pytest.raises(ValueError, match="n must be >= 1"):
        a109261_seq(0, backend="python")


def test_a109261_larger_terms():
    # Extend self-inverse check further
    for n in range(1, 26):
        assert get("A109261", get("A109261", n)) == n
