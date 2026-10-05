from bench.runner import run_sorting, run_sjf
from bench import plots

if __name__ == "__main__":
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
    df = run_sorting(sizes)
    plots.plot_sorting(df, "random", "sorting_random.png")
    plots.plot_sorting(df, "sorted", "sorting_sorted.png")
    plots.plot_sorting(df, "reversed", "sorting_reversed.png")
    plots.plot_distributions(df, "quick")
    plots.plot_distributions(df, "insertion")
    plots.plot_vs_theory(df, "insertion", "n2")
    plots.plot_vs_theory(df, "merge", "nlogn")

    dfs = run_sjf([100, 300, 1000, 3000, 10000])
    plots.plot_sjf(dfs)
    print(df.pivot_table(index="n", columns="algo", values="time", aggfunc="mean"))
    print(dfs)