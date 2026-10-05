import random

def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    l, r = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

def quick_sort(a):
    if len(a) <= 1:
        return a[:]
    p = random.choice(a)  # A random pivot protects against O(n^2) on sorted data
    less = [x for x in a if x < p]
    eq = [x for x in a if x == p]
    more = [x for x in a if x > p]
    return quick_sort(less) + eq + quick_sort(more)

def builtin_sort(a):
    return sorted(a)  # Timsort, a benchmark

ALGORITHMS = {
    "bubble": bubble_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "builtin": builtin_sort,
}