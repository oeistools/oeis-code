# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

from typing import Any, Literal

from .backends import pari as pari_backend
from .registry import registry

BackendType = Literal["auto", "pari", "python"]


def get(seq_id: str, n: int, backend: BackendType = "auto") -> Any:
    """
    Get the n-th term of an OEIS sequence.

    Args:
        seq_id: The OEIS identifier (e.g., 'A000045').
        n: The index of the term to retrieve.
        backend: The backend to use ('auto', 'pari', or 'python').
            'auto' will prioritize PARI/GP if available.

    Returns:
        The n-th term of the sequence.

    Raises:
        ValueError: If the sequence ID is not found in the registry.
    """
    if seq_id not in registry:
        raise ValueError(f"Sequence {seq_id} not implemented")

    func = registry[seq_id]

    if backend == "auto":
        try:
            if pari_backend.AVAILABLE:
                return func(n, backend="pari")
        except Exception:
            pass
        return func(n, backend="python")

    return func(n, backend=backend)
