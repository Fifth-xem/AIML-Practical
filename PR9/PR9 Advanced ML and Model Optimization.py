import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# 1. Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

print("Dataset: Breast Cancer Wisconsin")
print("Total samples:", X.shape[0])
print("Total features:", X.shape[1])

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Define models and parameter grids
models = {
    "SVM": (
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", SVC())
        ]),
        {
            "model__C": [0.1, 1, 10],
            "model__kernel": ["linear", "rbf"]
        }
    ),

    "Random Forest": (
        RandomForestClassifier(random_state=42),
        {
            "n_estimators": [50, 100],
            "max_depth": [None, 5, 10]
        }
    ),

    "AdaBoost": (
        AdaBoostClassifier(random_state=42),
        {
            "n_estimators": [50, 100],
            "learning_rate": [0.5, 1.0]
        }
    )
}

results = []

# 4. Train, evaluate and optimize each model
for name, (model, params) in models.items():

    print("\nProcessing:", name)

    # Before optimization
    model.fit(X_train, y_train)
    pred_before = model.predict(X_test)

    before_accuracy = accuracy_score(y_test, pred_before)
    before_precision = precision_score(
        y_test, pred_before, zero_division=0
    )
    before_recall = recall_score(
        y_test, pred_before, zero_division=0
    )
    before_f1 = f1_score(
        y_test, pred_before, zero_division=0
    )

    # Hyperparameter tuning using 5-fold cross-validation
    grid = GridSearchCV(
        estimator=model,
        param_grid=params,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    # After optimization
    best_model = grid.best_estimator_
    pred_after = best_model.predict(X_test)

    after_accuracy = accuracy_score(y_test, pred_after)
    after_precision = precision_score(
        y_test, pred_after, zero_division=0
    )
    after_recall = recall_score(
        y_test, pred_after, zero_division=0
    )
    after_f1 = f1_score(
        y_test, pred_after, zero_division=0
    )

    # Store results
    results.append({
        "Model": name,
        "Accuracy Before (%)": round(before_accuracy * 100, 2),
        "Accuracy After (%)": round(after_accuracy * 100, 2),
        "Precision Before": round(before_precision, 4),
        "Precision After": round(after_precision, 4),
        "Recall Before": round(before_recall, 4),
        "Recall After": round(after_recall, 4),
        "F1 Before": round(before_f1, 4),
        "F1 After": round(after_f1, 4),
        "Best CV Accuracy (%)": round(grid.best_score_ * 100, 2),
        "Best Parameters": str(grid.best_params_)
    })

# 5. Create separate comparison tables
df = pd.DataFrame(results)

print("\n" + "=" * 65)
print("TABLE 1: ACCURACY COMPARISON")
print("=" * 65)

print(df[[
    "Model",
    "Accuracy Before (%)",
    "Accuracy After (%)"
]].to_string(index=False))

print("\n" + "=" * 65)
print("TABLE 2: PRECISION COMPARISON")
print("=" * 65)

print(df[[
    "Model",
    "Precision Before",
    "Precision After"
]].to_string(index=False))

print("\n" + "=" * 65)
print("TABLE 3: F1-SCORE COMPARISON")
print("=" * 65)

print(df[[
    "Model",
    "F1 Before",
    "F1 After"
]].to_string(index=False))

# 6. Display cross-validation accuracy
print("\n" + "=" * 65)
print("TABLE 4: GRID SEARCH RESULTS")
print("=" * 65)

print(df[[
    "Model",
    "Best CV Accuracy (%)",
    "Best Parameters"
]].to_string(index=False))

print("\nPractical completed successfully!")
