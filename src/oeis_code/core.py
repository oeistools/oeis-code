# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""Public entry point: ``get`` dispatches a request to a registered sequence."""

from typing import Any, Literal

from .backends import pari as pari_backend
from .registry import registry

BackendType = Literal["auto", "pari", "python"]


def get(seq_id: str, n: int, backend: BackendType = "auto") -> Any:
    """
    Get the n-th term of an OEIS sequence.

    Parameters
    ----------
    seq_id : str
        The OEIS identifier (e.g., 'A000045').
    n : int
        The index of the term to retrieve.
    backend : {'auto', 'pari', 'python'}, default 'auto'
        The backend to use. 'auto' will prioritize PARI/GP if available.

    Returns
    -------
    Any
        The n-th term of the sequence.

    Raises
    ------
    ValueError
        If the sequence ID is not found in the registry.
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
