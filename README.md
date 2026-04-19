# oeis-code

Mini OEIS in Python with PARI/GP support.

## Installation

```bash
pip install cypari2  # optional
```

## Usage

```python
from oeis_code import get

# Get the first 10 Fibonacci numbers
get("A000045", 10)
```

## Contributing

- Create a new file in `oeis_code/sequences/`
- Use the `@register("Axxxxxx")` decorator
- Implement the `sequence(n)` function
