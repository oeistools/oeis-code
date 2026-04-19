
from .registry import registry
from .backends import pari as pari_backend
from .backends import python as py_backend

def get(seq_id, n, backend="auto"):
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
