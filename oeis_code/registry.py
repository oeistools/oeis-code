from typing import Any, Callable, Dict

registry: Dict[str, Callable[..., Any]] = {}

def register(seq_id: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator to register a sequence function in the registry.

    Args:
        seq_id: The OEIS sequence identifier (e.g., 'A000045').

    Returns:
        The decorator function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        registry[seq_id] = func
        return func
    return decorator
