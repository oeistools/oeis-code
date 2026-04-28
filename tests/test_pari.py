# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

import pytest

from oeis_code import get
from oeis_code.backends import pari as pari_backend


def test_pari_status():
    """Check if PARI is available in the current environment."""
    print(f"PARI available: {pari_backend.AVAILABLE}")


@pytest.mark.skipif(
    pari_backend.AVAILABLE, reason="PARI is available, skipping fallback tests"
)
def test_pari_not_available_fallback():
    """
    Test fallback behavior when PARI/GP is NOT available.
    """
    assert not pari_backend.AVAILABLE
    assert pari_backend.pari is None

    # backend="auto" should work (fallback to python)
    assert get("A000045", 10, backend="auto") == 55

    # Explicitly asking for pari should raise ImportError
    with pytest.raises(ImportError, match="The PARI/GP backend is not available"):
        pari_backend.fibonacci(10)


@pytest.mark.skipif(
    not pari_backend.AVAILABLE, reason="PARI is NOT available, skipping backend tests"
)
def test_pari_available_functionality():
    """
    Test backend functionality when PARI/GP IS available.
    """
    assert pari_backend.AVAILABLE
    assert pari_backend.pari is not None

    # Test direct backend calls
    assert pari_backend.fibonacci(10) == 55
    assert pari_backend.prime(1) == 2
    assert pari_backend.prime(5) == 11

    # Test through core get()
    assert get("A000045", 10, backend="pari") == 55
    assert get("A000040", 5, backend="pari") == 11


def test_pari_auto_backend():
    """
    Test that backend='auto' always works regardless of PARI availability.
    """
    # This should work in both cases
    assert get("A000045", 10, backend="auto") == 55
    assert get("A000040", 5, backend="auto") == 11
