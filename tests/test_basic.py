# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

import pytest

from oeis_code import get


def test_fibonacci():
    assert get("A000045", 0) == 0
    assert get("A000045", 1) == 1
    assert get("A000045", 5) == 5
    assert get("A000045", 10) == 55


def test_primes():
    assert get("A000040", 1) == 2
    assert get("A000040", 5) == 11


def test_invalid_sequence():
    with pytest.raises(ValueError, match="Sequence A999999 not implemented"):
        get("A999999", 5)


def test_backends():
    # Test explicit python backend
    assert get("A000045", 5, backend="python") == 5

    # Test auto backend
    assert get("A000045", 5, backend="auto") == 5
