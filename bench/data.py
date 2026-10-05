import random

def random_data(n):
    return [random.randint(0, n * 10) for _ in range(n)]

def sorted_data(n):
    return list(range(n))

def reversed_data(n):
    return list(range(n, 0, -1))

def nearly_sorted(n, swaps=None):
    a = list(range(n))
    for _ in range(swaps or max(1, n // 100)):
        i, j = random.randrange(n), random.randrange(n)
        a[i], a[j] = a[j], a[i]
    return a

def processes(n):
    return [(i, random.randint(0, n), random.randint(1, 20)) for i in range(n)]

GENERATORS = {
    "random": random_data,
    "sorted": sorted_data,
    "reversed": reversed_data,
    "nearly_sorted": nearly_sorted,
}