"""Compare four classifiers on the Breast Cancer dataset with cross-validation."""
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def main():
    X, y = load_breast_cancer(return_X_y=True)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    models = {
        "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
        "k-NN (k=5)": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
        "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    }

    print(f"{'Model':<22} {'mean acc':>8} {'std':>6}")
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=cv)
        print(f"{name:<22} {scores.mean():>8.3f} {scores.std():>6.3f}")


if __name__ == "__main__":
    main()
