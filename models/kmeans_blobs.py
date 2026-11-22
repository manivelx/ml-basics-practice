"""K-Means clustering on synthetic blobs.

Compares k = 2..6 with inertia (elbow method) and silhouette score, then saves
a scatter plot of the best clustering to outputs/kmeans_clusters.png.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score


def main():
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.9, random_state=7)

    print("k | inertia  | silhouette")
    best_k, best_score = 2, -1.0
    for k in range(2, 7):
        model = KMeans(n_clusters=k, n_init=10, random_state=7).fit(X)
        score = silhouette_score(X, model.labels_)
        print(f"{k} | {model.inertia_:8.1f} | {score:.3f}")
        if score > best_score:
            best_k, best_score = k, score
    print(f"\nBest k by silhouette: {best_k}")

    model = KMeans(n_clusters=best_k, n_init=10, random_state=7).fit(X)
    out_dir = Path(__file__).resolve().parent.parent / "outputs"
    out_dir.mkdir(exist_ok=True)
    plt.scatter(X[:, 0], X[:, 1], c=model.labels_, s=15, cmap="viridis")
    plt.scatter(*model.cluster_centers_.T, c="red", marker="x", s=100)
    plt.title(f"K-Means with k={best_k}")
    plt.savefig(out_dir / "kmeans_clusters.png", dpi=120, bbox_inches="tight")
    print(f"Saved plot to {out_dir / 'kmeans_clusters.png'}")


if __name__ == "__main__":
    main()
