import random
import pytest
from algorithms.sorting import ALGORITHMS
from algorithms.sjf import sjf_naive, sjf_heap

@pytest.mark.parametrize("name", ALGORITHMS)
def test_sorting(name):
    for n in (0, 1, 2, 50, 300):
        a = [random.randint(-100, 100) for _ in range(n)]
        assert ALGORITHMS[name](a) == sorted(a)

def test_sjf_same_waiting():
    procs = [(i, random.randint(0, 50), random.randint(1, 10)) for i in range(100)]
    w1 = sum(r[2] for r in sjf_naive(procs))
    w2 = sum(r[2] for r in sjf_heap(procs))
    assert w1 == w2