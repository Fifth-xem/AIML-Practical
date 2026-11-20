# Practical No. 9: Advanced Machine Learning and Model Optimization

## 1. Aim

To implement and compare Support Vector Machine (SVM), Random Forest and AdaBoost algorithms. Perform cross-validation and hyperparameter tuning using Grid Search, and evaluate model performance before and after optimization.

## 2. Dataset Used

**Dataset:** Breast Cancer Wisconsin Dataset

This practical uses the Breast Cancer Wisconsin dataset provided by Scikit-learn.

- Total samples: 569
- Total features: 30
- Type: Binary Classification
- Classes: Malignant and Benign

### Dataset Loading

```python
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data
y = data.target
```

`load_breast_cancer()` loads the built-in dataset directly from Scikit-learn.

- `X` contains the input features.
- `y` contains the target class labels.

No external CSV file is required when using this method.

## 3. Explanation of the Code

### Step 1: Import Required Libraries

```python
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
```

- Pandas: Creates tables for comparing model results.
- Scikit-learn: Provides machine learning algorithms and utilities.
- GridSearchCV: Performs cross-validation and hyperparameter tuning.
- StandardScaler: Standardizes features for SVM.
- Pipeline: Combines scaling and SVM into one workflow.
- SVC: Implements Support Vector Machine.
- RandomForestClassifier: Implements Random Forest.
- AdaBoostClassifier: Implements AdaBoost.
- Evaluation metrics: Calculate accuracy, precision, recall and F1-score.

### Step 2: Load the Dataset

```python
data = load_breast_cancer()
X = data.data
y = data.target
```

The dataset is loaded into memory.

- X represents the 30 input features.
- y represents the corresponding output classes.

The program also displays the total number of samples and features.

### Step 3: Split the Dataset

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

The dataset is divided into:

- 80% training data to train the models.
- 20% testing data to evaluate their performance.

`random_state=42` ensures reproducible results.

`stratify=y` maintains the proportion of both classes in the training and testing sets.

### Step 4: Define Machine Learning Models

Three algorithms are defined:

**1. Support Vector Machine (SVM)**

SVM is a supervised learning algorithm that finds the best separating hyperplane between classes by maximizing the margin.

It uses StandardScaler to normalize features before classification.

Parameters tuned:
- C: Controls the penalty for classification errors.
- Kernel: Specifies the type of decision boundary, such as linear or RBF.

**2. Random Forest**

Random Forest is an ensemble learning algorithm that combines multiple decision trees and uses majority voting for classification.

Parameters tuned:
- n_estimators: Number of decision trees.
- max_depth: Maximum depth of each tree.

**3. AdaBoost**

AdaBoost (Adaptive Boosting) is an ensemble learning algorithm that combines multiple weak learners to create a stronger classifier. It gives more attention to incorrectly classified samples during training.

Parameters tuned:
- n_estimators: Number of weak learners.
- learning_rate: Controls the contribution of each learner.

### Step 5: Train and Evaluate Models Before Optimization

```python
model.fit(X_train, y_train)
pred_before = model.predict(X_test)
```

Each model is initially trained using its default parameters.

Predictions are made on the testing dataset and evaluated using:

- Accuracy: Percentage of correctly classified samples.
- Precision: Proportion of positive predictions that are correct.
- Recall: Proportion of actual positive samples correctly identified.
- F1-score: Harmonic mean of precision and recall.

These values represent the model's performance before optimization.

### Step 6: Cross-Validation and Hyperparameter Tuning

```python
grid = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X_train, y_train)
```

Grid Search tests different combinations of hyperparameters to find the best-performing configuration.

**5-Fold Cross-Validation:**

1. Training data is divided into five folds.
2. Four folds are used for training.
3. One fold is used for validation.
4. This process is repeated five times, using a different validation fold each time.
5. The average validation accuracy is calculated.

`best_estimator_` returns the model with the best parameters, while `best_score_` provides its best average cross-validation accuracy.

### Step 7: Evaluate Models After Optimization

```python
best_model = grid.best_estimator_
pred_after = best_model.predict(X_test)
```

The optimized model is used to predict the testing data again.

Accuracy, precision, recall and F1-score are calculated once more.

These results are compared with the original model performance to understand the effect of hyperparameter tuning.

### Step 8: Compare Model Performance

The results are stored in a Pandas DataFrame.

The program displays four comparison tables:

1. Accuracy Comparison: Compares accuracy before and after optimization.
2. Precision Comparison: Compares precision before and after optimization.
3. F1-Score Comparison: Compares F1-score before and after optimization.
4. Grid Search Results: Displays the best cross-validation accuracy and selected hyperparameters.

The Recall values are also calculated and stored in the DataFrame. They can be displayed using an additional comparison table.

## 4. Evaluation Metrics

| Metric | Meaning |
|---|---|
| Accuracy | Overall percentage of correct predictions. |
| Precision | How many predicted positive cases are actually positive. |
| Recall | How many actual positive cases are correctly identified. |
| F1-score | Balance between precision and recall. |
| Cross-validation accuracy | Average validation accuracy across five folds. |

## 5. Result

The three algorithms, SVM, Random Forest and AdaBoost, were successfully implemented and compared.

Cross-validation and Grid Search were used to identify suitable hyperparameters for each model.

The performance of each model was evaluated before and after optimization using accuracy, precision, recall and F1-score.

The results showed that SVM achieved the highest test accuracy of 98.25% in the given execution.

Optimization did not necessarily improve the test accuracy because the selected hyperparameters can produce the same predictions as the default model.

**Conclusion:** The practical successfully demonstrates advanced machine learning algorithms, cross-validation, hyperparameter optimization and model performance comparison.
