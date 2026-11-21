# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""Mini OEIS: compute OEIS sequence terms with a PARI/GP or pure-Python backend."""

__version__ = "0.1.0"

from . import sequences
from .core import get

__all__ = ["get", "sequences"]
