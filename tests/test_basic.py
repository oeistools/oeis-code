# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

import pytest

from oeis_code import get
from oeis_code.utils.math import fibonacci_term, is_prime


# ---------------------------------------------------------------------------
# A000045 — Fibonacci numbers
# ---------------------------------------------------------------------------


def test_fibonacci_base_cases():
    assert get("A000045", 0) == 0
    assert get("A000045", 1) == 1


def test_fibonacci_values():
    assert get("A000045", 5) == 5
    assert get("A000045", 10) == 55
    assert get("A000045", 20) == 6765


# ---------------------------------------------------------------------------
# A000040 — Prime numbers
# ---------------------------------------------------------------------------


def test_primes():
    assert get("A000040", 1) == 2
    assert get("A000040", 2) == 3
    assert get("A000040", 5) == 11
    assert get("A000040", 10) == 29


# ---------------------------------------------------------------------------
# A000120 — Hamming weight (number of 1-bits)
# ---------------------------------------------------------------------------


def test_hamming_weight():
    assert get("A000120", 0) == 0   # 0b0
    assert get("A000120", 1) == 1   # 0b1
    assert get("A000120", 5) == 2   # 0b101
    assert get("A000120", 7) == 3   # 0b111
    assert get("A000120", 255) == 8  # 0b11111111


# ---------------------------------------------------------------------------
# A016993 — a(n) = 7n + 1
# ---------------------------------------------------------------------------


def test_A016993():
    assert get("A016993", 0) == 1
    assert get("A016993", 1) == 8
    assert get("A016993", 5) == 36
    assert get("A016993", 10) == 71


# ---------------------------------------------------------------------------
# A017053 — a(n) = 7n + 6
# ---------------------------------------------------------------------------


def test_A017053():
    assert get("A017053", 0) == 6
    assert get("A017053", 1) == 13
    assert get("A017053", 5) == 41
    assert get("A017053", 10) == 76


# ---------------------------------------------------------------------------
# A066096 — Lower Wythoff sequence: floor(n * phi)
# ---------------------------------------------------------------------------


def test_lower_wythoff():
    # A066096: 0, 1, 3, 4, 6, 8, 9, 11, 12, 14, ...
    expected = {0: 0, 1: 1, 2: 3, 3: 4, 4: 6, 5: 8}
    for n, val in expected.items():
        assert get("A066096", n) == val


# ---------------------------------------------------------------------------
# utils.math — is_prime edge cases
# ---------------------------------------------------------------------------


def test_is_prime_small():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)


def test_is_prime_even():
    assert not is_prime(100)
    assert not is_prime(1000)


def test_is_prime_divisible_by_3():
    assert not is_prime(9)
    assert not is_prime(15)


def test_is_prime_large():
    assert is_prime(97)
    assert is_prime(997)
    assert not is_prime(999)


# ---------------------------------------------------------------------------
# utils.math — fibonacci_term edge cases
# ---------------------------------------------------------------------------


def test_fibonacci_term_zero():
    assert fibonacci_term(0) == 0


def test_fibonacci_term_one():
    assert fibonacci_term(1) == 1


def test_fibonacci_term_sequence():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, val in enumerate(expected):
        assert fibonacci_term(i) == val


# ---------------------------------------------------------------------------
# Core API
# ---------------------------------------------------------------------------


def test_invalid_sequence():
    with pytest.raises(ValueError, match="Sequence A999999 not implemented"):
        get("A999999", 5)


def test_explicit_python_backend():
    assert get("A000045", 5, backend="python") == 5


def test_auto_backend():
    assert get("A000045", 5, backend="auto") == 5
