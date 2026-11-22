"""k-Nearest Neighbours on the Iris dataset.

Picks k with 5-fold cross-validation on the training set only, then reports
accuracy on a held-out test set.
"""
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def build_model(k):
    # Scaling lives inside the pipeline so it is fitted on training folds only.
    return make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))


def main():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    print("k  | 5-fold CV accuracy")
    best_k, best_score = 1, 0.0
    for k in range(1, 16, 2):
        score = cross_val_score(build_model(k), X_train, y_train, cv=5).mean()
        print(f"{k:<2} | {score:.3f}")
        if score > best_score:
            best_k, best_score = k, score

    model = build_model(best_k).fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"\nBest k: {best_k}")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.3f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))


if __name__ == "__main__":
    main()
