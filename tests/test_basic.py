
from oeis_code import get

def test_fibonacci():
    assert get("A000045", 5) == [0,1,1,2,3]

def test_primes():
    assert get("A000040", 5) == [2,3,5,7,11]
