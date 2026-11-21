# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Enrique Pérez Herrero

"""Registry mapping OEIS identifiers to their sequence functions."""

from typing import Any, Callable

registry: dict[str, Callable[..., Any]] = {}


def register(seq_id: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Return a decorator that registers a sequence function under ``seq_id``.

    Parameters
    ----------
    seq_id : str
        The OEIS sequence identifier (e.g., 'A000045').

    Returns
    -------
    Callable[[Callable[..., Any]], Callable[..., Any]]
        The decorator, which stores the decorated function in ``registry``
        and returns it unchanged.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Store ``func`` in the registry under ``seq_id`` and return it."""
        registry[seq_id] = func
        return func

    return decorator
