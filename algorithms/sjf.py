import heapq

# process = (pid, arrival, burst)

def sjf_naive(procs):
    """not a priority SJF, min linear : O(n^2)."""
    remaining = sorted(procs, key=lambda p: p[1])
    time, result = 0, []
    while remaining:
        ready = [p for p in remaining if p[1] <= time]
        if not ready:
            time = min(p[1] for p in remaining)
            continue
        job = min(ready, key=lambda p: p[2])
        remaining.remove(job)
        time += job[2]
        result.append((job[0], time - job[1], time - job[1] - job[2]))  # pid, turnaround, waiting
    return result

def sjf_heap(procs):
    """The same SJF, but with a whole lot of: O(n log n)."""
    procs = sorted(procs, key=lambda p: p[1])
    heap, i, time, result = [], 0, 0, []
    while i < len(procs) or heap:
        if not heap and procs[i][1] > time:
            time = procs[i][1]
        while i < len(procs) and procs[i][1] <= time:
            pid, arr, burst = procs[i]
            heapq.heappush(heap, (burst, arr, pid))
            i += 1
        burst, arr, pid = heapq.heappop(heap)
        time += burst
        result.append((pid, time - arr, time - arr - burst))
    return result

def avg_waiting(result):
    return sum(r[2] for r in result) / len(result)