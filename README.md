# oeis-code

[![CI](https://github.com/oeistools/oeis-code/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/oeistools/oeis-code/actions/workflows/tests.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/oeistools/oeis-code/graph/badge.svg)](https://codecov.io/gh/oeistools/oeis-code)
[![PyPI version](https://img.shields.io/pypi/v/oeis-code.svg)](https://pypi.org/project/oeis-code/)
[![Python versions](https://img.shields.io/pypi/pyversions/oeis-code.svg?logo=python&logoColor=white)](https://pypi.org/project/oeis-code/)
[![Package format](https://img.shields.io/pypi/format/oeis-code.svg?logo=pypi&logoColor=white)](https://pypi.org/project/oeis-code/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue?logo=readthedocs&logoColor=white)](https://oeistools.github.io/oeis-code/)

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

- Create a new file in `src/oeis_code/sequences/`
- Use the `@register("Axxxxxx")` decorator
- Implement the `sequence(n)` function
- See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidance

## Releases

See [CHANGELOG.md](CHANGELOG.md) for a full list of changes.
