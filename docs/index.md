# oeis-code

Mini OEIS in Python with PARI/GP support.

## Overview

Welcome to the `oeis-code` documentation. This library allows you to interact with the Online Encyclopedia of Integer Sequences (OEIS) programmatically using native Python and PARI/GP backends.

## Quick Start

```bash
pip install oeis-code
```

```python
from oeis_code import get

# Get the 10th Fibonacci number
get("A000045", 10)  # Returns 55
```

Check out the [Usage Guide](usage.md) and the [API Reference](reference/core.md) to see all the available classes and functions.
