# ML Basics Practice

Small, runnable scripts I wrote while learning Python and machine learning. Each file does one thing and prints its result, so it is easy to read and re-run.

## Layout

| Path | What it covers |
|---|---|
| `python-basics/basics.py` | FizzBuzz, palindrome check, word frequency, grading with dicts and functions |
| `tests/test_basics.py` | `pytest` tests for the functions in `basics.py` |
| `lists_functions.py`, `list_comprehension.py` | Lists, functions, list comprehensions |
| `numpy_basics.py` | Arrays, mean, standard deviation, reshaping |
| `pandas_basics.py` | DataFrames, filtering, new columns |
| `matplotlib_practice.py` | Scatter and line plot of study hours vs marks |
| `linear_regression.py` | Linear regression on a tiny study-hours dataset |
| `logistic_regression.py` | Logistic regression on a pass/fail example |
| `models/knn_iris.py` | k-NN on Iris, choosing k with cross-validation |
| `models/decision_tree_wine.py` | Decision tree depth vs over-fitting on the Wine dataset |
| `models/kmeans_blobs.py` | K-Means with elbow and silhouette score, saves a plot |
| `models/model_comparison.py` | Four classifiers compared with 5-fold cross-validation |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python models/knn_iris.py
python models/decision_tree_wine.py
python models/kmeans_blobs.py       # writes outputs/kmeans_clusters.png
python models/model_comparison.py
python python-basics/basics.py
pytest
```

The `models/` scripts use datasets that ship with scikit-learn, so no download is needed.

## What I practised

- Splitting data into train and test sets and keeping the test set unseen
- Putting scaling inside a `Pipeline` so it never sees test data
- Choosing a hyperparameter (k, tree depth) with cross-validation instead of guessing
- Comparing models fairly with the same folds

## Next

- A neural network example with scikit-learn's `MLPClassifier`
- Feature engineering on a real tabular dataset
- See [loan-approval-prediction](https://github.com/manivelx/loan-approval-prediction) for a complete small project
