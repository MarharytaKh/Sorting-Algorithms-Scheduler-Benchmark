A Python project that measures the running time of sorting algorithms (bubble, insertion, merge, quick, and built-in sorted) and the SJF scheduling algorithm
(naive vs. heap-based) on growing inputs of different types (random, sorted, reversed, nearly sorted). Results are saved to CSV and visualized with plots,
and the measured times are compared against theoretical
complexity (O(n²) vs. O(n log n)). Correctness of all implementations is verified with unit tests.
The experiments confirmed the theory: when n doubles, bubble and insertion sort slow down roughly 4×,
while merge and quick sort slow down roughly 2×. Using a heap speeds up SJF by about 400× on 10,000 processes.
