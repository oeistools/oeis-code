# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""
A109261 - Self-inverse permutation induced by Beatty sequences for
          alpha = sqrt(2)^sqrt(2) and beta = alpha/(alpha-1).
https://oeis.org/A109261
"""

import math
from functools import lru_cache
from typing import Literal

from ..backends import pari as pari_backend
from ..registry import register

# Beatty complementary pair: 1/alpha + 1/beta = 1
_alpha = math.sqrt(2) ** math.sqrt(2)
_beta = _alpha / (_alpha - 1)


@register("A109261")
@lru_cache(maxsize=256)
def sequence(n: int, backend: Literal["python", "pari"] = "python") -> int:
    """
    Self-inverse permutation induced by the Beatty sequences for
    alpha = sqrt(2)^sqrt(2) and beta = alpha/(alpha-1).

    The positive integers are partitioned into:
      - Sequence A: {floor(k*alpha) : k >= 1}
      - Sequence B: {floor(k*beta)  : k >= 1}

    a(n) = floor(k*beta)  if n = floor(k*alpha) for some k,
    a(n) = floor(k*alpha) if n = floor(k*beta)  for some k.

    A109261: 2, 1, 5, 7, 3, 9, 4, 11, 6, 13, 8, 15, 10, 17, 12, ...

    Args:
        n: The positive integer index (1-indexed).
        backend: Computation backend ('python' or 'pari').

    Returns:
        a(n), the n-th term of the permutation.

    Raises:
        ValueError: If n < 1.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    if backend == "pari" and pari_backend.AVAILABLE:
        # Use PARI/GP floor for exact integer arithmetic
        alpha_str = "sqrt(2)^sqrt(2)"
        beta_str = f"({alpha_str}) / ({alpha_str} - 1)"
        ka = int(n / _alpha) + 2
        kb = int(n / _beta) + 2
        for k in range(max(1, ka - 3), ka + 4):
            if int(pari_backend.pari(f"floor({k}*({alpha_str}))")) == n:
                return int(pari_backend.pari(f"floor({k}*({beta_str}))"))
        for k in range(max(1, kb - 3), kb + 4):
            if int(pari_backend.pari(f"floor({k}*({beta_str}))")) == n:
                return int(pari_backend.pari(f"floor({k}*({alpha_str}))"))
        raise RuntimeError(f"Term not found for n={n}")

    # Python backend: search a small window around the estimated index
    ka = int(n / _alpha) + 2
    kb = int(n / _beta) + 2

    for k in range(max(1, ka - 3), ka + 4):
        if math.floor(k * _alpha) == n:
            return math.floor(k * _beta)

    for k in range(max(1, kb - 3), kb + 4):
        if math.floor(k * _beta) == n:
            return math.floor(k * _alpha)

    raise RuntimeError(f"Term not found for n={n}")
