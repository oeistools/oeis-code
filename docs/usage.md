# Usage Guide

This guide covers the core functionalities of `oeis-code`.

## Getting Sequence Terms

The primary interface is the `get()` function. It evaluates the sequence at a given index.

```python
from oeis_code import get

# Get the 10th Fibonacci number
val = get("A000045", 10)
print(val) # 55
```

## Adding Sequences

To add sequences to `oeis-code`, you register them in the `src/oeis_code/sequences/` directory:

```python
from oeis_code.registry import register

@register("A000045")
def sequence(n):
    if n <= 1:
        return n
    return sequence(n - 1) + sequence(n - 2)
```

## Backends

`oeis-code` provides fallbacks and PARI/GP bindings for high performance sequence calculations. Ensure you have `pari-gp` installed on your system to take advantage of the advanced `cypari2` backend.
