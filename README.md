# oeis-code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://github.com/oeistools/oeis-code/actions/workflows/tests.yml/badge.svg)](https://github.com/oeistools/oeis-code/actions/workflows/tests.yml)
[![Linting](https://github.com/oeistools/oeis-code/actions/workflows/lint.yml/badge.svg)](https://github.com/oeistools/oeis-code/actions/workflows/lint.yml)

Mini OEIS in Python with PARI/GP support.

## Installation

```bash
pip install oeis-code
```

### PARI/GP Support (Optional)

To use the PARI/GP backend, you need `cypari2`. Note that this requires PARI/GP development headers installed on your system.

**Debian/Ubuntu:**
```bash
sudo apt install build-essential python3-dev libgmp-dev libpari-dev pari-gp
pip install cypari2
```

**Fedora:**
```bash
sudo dnf install pari-devel
pip install cypari2
```

**macOS (using Homebrew):**
```bash
brew install pari
pip install cypari2
```

## Usage

```python
from oeis_code import get

# Get the 10th Fibonacci number
get("A000045", 10)  # Returns 55
```

## Contributing

- Create a new file in `oeis_code/sequences/`
- Use the `@register("Axxxxxx")` decorator
- Implement the `sequence(n)` function
