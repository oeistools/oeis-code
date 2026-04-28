# Contributing to oeis-code

## Development Setup

```bash
git clone https://github.com/oeistools/oeis-code.git
cd oeis-code
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Local Checks

Run these checks before opening a pull request:

```bash
ruff format .
ruff check . --fix
pytest -q
python -m build
python -m twine check dist/*
```

## Adding a New Sequence

1. Create a new file in `src/oeis_code/sequences/` named after the OEIS identifier, e.g. `A012345.py`.
2. Use the `@register("Axxxxxx")` decorator to register it in the sequence registry.
3. Implement the `sequence(n, backend)` function following the existing pattern.

```python
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A012345 - Description of the sequence.
https://oeis.org/A012345
"""

from functools import lru_cache
from typing import Literal

from ..registry import register


@register("A012345")
@lru_cache(maxsize=128)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Get the n-th term of A012345.
    """
    return ...  # your implementation here
```

4. Add at least one test in `tests/test_basic.py` covering key values.
5. Run `pytest -q` to make sure everything passes.

## Pull Requests

- Keep PRs focused on one change set.
- Add or update tests for behavioral changes.
- Update `README.md` when user-facing behavior changes.
- Ensure GitHub Actions checks are green.
