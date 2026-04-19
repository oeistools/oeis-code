
def primes(n):
    res = []
    num = 2
    while len(res) < n:
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            res.append(num)
        num += 1
    return res

def fibonacci(n):
    a, b = 0, 1
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res
