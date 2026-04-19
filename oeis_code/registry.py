
registry = {}

def register(seq_id):
    def decorator(func):
        registry[seq_id] = func
        return func
    return decorator
