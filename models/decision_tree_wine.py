"""Decision tree on the Wine dataset: how tree depth affects over-fitting."""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    data = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.3, random_state=42, stratify=data.target
    )

    print("depth | train acc | test acc")
    for depth in (1, 2, 3, 4, 6, None):
        tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
        tree.fit(X_train, y_train)
        label = "None" if depth is None else str(depth)
        print(f"{label:<5} | {tree.score(X_train, y_train):.3f}     | {tree.score(X_test, y_test):.3f}")

    # Feature importances from a shallow tree are easy to read.
    tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
    ranked = sorted(zip(data.feature_names, tree.feature_importances_), key=lambda p: -p[1])
    print("\nTop features (max_depth=3):")
    for name, importance in ranked[:5]:
        print(f"  {name:<22} {importance:.3f}")


if __name__ == "__main__":
    main()
