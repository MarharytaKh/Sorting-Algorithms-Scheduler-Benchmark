import time
import statistics
import pandas as pd
from algorithms.sorting import ALGORITHMS
from algorithms.sjf import sjf_naive, sjf_heap
from bench.data import GENERATORS, processes

def measure(func, data, repeats=5):
    times = []
    for _ in range(repeats):
        t = time.perf_counter()
        func(data)
        times.append(time.perf_counter() - t)
    return statistics.median(times)

def run_sorting(sizes, repeats=5, slow_limit=3000):
    rows = []
    for dist, gen in GENERATORS.items():
        for n in sizes:
            data = gen(n)
            for name, func in ALGORITHMS.items():
                if name in ("bubble", "insertion") and n > slow_limit:
                    continue  # O(n^2) too much time om big n
                rows.append(dict(algo=name, dist=dist, n=n, time=measure(func, data, repeats)))
    df = pd.DataFrame(rows)
    df.to_csv("results_sorting.csv", index=False)
    return df

def run_sjf(sizes, repeats=3):
    rows = []
    for n in sizes:
        data = processes(n)
        for name, func in (("sjf_naive", sjf_naive), ("sjf_heap", sjf_heap)):
            rows.append(dict(algo=name, n=n, time=measure(func, data, repeats)))
    df = pd.DataFrame(rows)
    df.to_csv("results_sjf.csv", index=False)
    return df