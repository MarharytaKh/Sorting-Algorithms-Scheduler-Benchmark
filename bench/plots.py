import numpy as np
import matplotlib.pyplot as plt

def plot_sorting(df, dist="random", out="sorting_random.png"):
    d = df[df.dist == dist]
    plt.figure(figsize=(8, 5))
    for algo, g in d.groupby("algo"):
        plt.plot(g.n, g.time, marker="o", label=algo)
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("n"); plt.ylabel("time, с")
    plt.title(f"Sort, data: {dist}")
    plt.legend(); plt.grid(True, which="both", alpha=.3)
    plt.savefig(out, dpi=150, bbox_inches="tight"); plt.close()

def plot_distributions(df, algo, out=None):
    d = df[df.algo == algo]
    plt.figure(figsize=(8, 5))
    for dist, g in d.groupby("dist"):
        plt.plot(g.n, g.time, marker="o", label=dist)
    plt.xscale("log"); plt.yscale("log")
    plt.title(f"{algo}: the effect of the type of input data")
    plt.xlabel("n"); plt.ylabel("time, с"); plt.legend(); plt.grid(True, alpha=.3)
    plt.savefig(out or f"dist_{algo}.png", dpi=150, bbox_inches="tight"); plt.close()

def plot_vs_theory(df, algo, complexity, out=None):
    """Comparison of the measured time with the theoretical curve (scaled to the last point."""
    g = df[(df.algo == algo) & (df.dist == "random")].sort_values("n")
    n, t = g.n.values, g.time.values
    f = {"n2": n**2, "nlogn": n * np.log2(n), "n": n}[complexity]
    theory = f * (t[-1] / f[-1])
    plt.figure(figsize=(8, 5))
    plt.plot(n, t, "o-", label="measured")
    plt.plot(n, theory, "--", label=f"theory O({complexity})")
    plt.xscale("log"); plt.yscale("log")
    plt.title(f"{algo}: experiment / theory")
    plt.xlabel("n"); plt.ylabel("time, с"); plt.legend(); plt.grid(True, alpha=.3)
    plt.savefig(out or f"theory_{algo}.png", dpi=150, bbox_inches="tight"); plt.close()

def plot_sjf(df, out="sjf.png"):
    plt.figure(figsize=(8, 5))
    for algo, g in df.groupby("algo"):
        plt.plot(g.n, g.time, marker="o", label=algo)
    plt.xscale("log"); plt.yscale("log")
    plt.title("SJF: naive implementation / a heap")
    plt.xlabel("number of processes"); plt.ylabel("time, с"); plt.legend(); plt.grid(True, alpha=.3)
    plt.savefig(out, dpi=150, bbox_inches="tight"); plt.close()