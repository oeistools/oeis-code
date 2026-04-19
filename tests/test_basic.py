import pytest

from oeis_code import get


def test_fibonacci():
    assert get("A000045", 0) == []
    assert get("A000045", 1) == [0]
    assert get("A000045", 5) == [0, 1, 1, 2, 3]
    assert get("A000045", 10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_primes():
    assert get("A000040", 0) == []
    assert get("A000040", 1) == [2]
    assert get("A000040", 5) == [2, 3, 5, 7, 11]


def test_invalid_sequence():
    with pytest.raises(ValueError, match="Sequence A999999 not implemented"):
        get("A999999", 5)


def test_backends():
    # Test explicit python backend
    assert get("A000045", 5, backend="python") == [0, 1, 1, 2, 3]

    # Test auto backend
    assert get("A000045", 5, backend="auto") == [0, 1, 1, 2, 3]
