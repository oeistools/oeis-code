
try:
    from cypari2 import Pari
    pari = Pari()
    AVAILABLE = True
except Exception:
    AVAILABLE = False

def prime(n):
    return int(pari(f"prime({n})"))

def fibonacci(n):
    return int(pari(f"fibonacci({n})"))
