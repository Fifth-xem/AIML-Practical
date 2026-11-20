# Practical No. 6 – Classification using Logistic Regression and K-Nearest Neighbors (KNN)

## 1. Aim

To perform data preprocessing and implement Logistic Regression and K-Nearest Neighbors (KNN) classification algorithms. Evaluate both models using Accuracy, Precision, Recall, F1-Score and Confusion Matrix, and compare their performance.

## 2. Dataset Used

**Dataset:** Heart Disease Dataset (`heart.csv`)

- Total records: 303
- Total columns: 14
- Input features: 13
- Target column: `target`

The target variable represents:
- `0` – No heart disease
- `1` – Presence of heart disease

The dataset is loaded from a local CSV file using Pandas:

```python
df = pd.read_csv("heart.csv")
```

**Important:** The `heart.csv` file must be present in the same directory as the Python program when using this relative path.

The dataset is not downloaded automatically from the internet or fetched using Scikit-learn.

## 3. Code Explanation

### Step 1: Import Required Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, ConfusionMatrixDisplay
)
```

- **Pandas:** Loads and manages the dataset.
- **Matplotlib:** Displays confusion matrix graphs.
- **train_test_split:** Divides the dataset into training and testing sets.
- **StandardScaler:** Performs feature scaling.
- **LogisticRegression:** Implements Logistic Regression.
- **KNeighborsClassifier:** Implements the KNN algorithm.
- **sklearn.metrics:** Calculates evaluation metrics and displays confusion matrices.

### Step 2: Load the Dataset

```python
df = pd.read_csv("heart.csv")
```

Loads the Heart Disease dataset into a Pandas DataFrame.

`df.head()` displays the first five records, while `df.shape` displays the number of rows and columns.

### Step 3: Check Missing Values

```python
print(df.isnull().sum())
```

Checks the number of missing values in each column.

Our dataset contains zero missing values, so no missing-value replacement is required.

### Step 4: Separate Features and Target

```python
X = df.drop("target", axis=1)
y = df["target"]
```

- `X` contains the 13 input features.
- `y` contains the target variable that we want to predict.

### Step 5: Split Data into Training and Testing Sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20,
    random_state=42, stratify=y
)
```

Divides the dataset into:

- 80% training data (242 records).
- 20% testing data (61 records).

`random_state=42` ensures reproducible splitting.

`stratify=y` maintains the class distribution in both sets.

### Step 6: Feature Scaling

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

StandardScaler standardizes the features so that they have comparable scales.

This is especially important for KNN because it uses distances to identify neighboring data points.

The scaler is fitted only on training data and then applied to testing data to prevent data leakage.

### Step 7: Implement Logistic Regression

```python
lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train_scaled, y_train)

y_pred_lr = lr_model.predict(X_test_scaled)
```

Logistic Regression is a supervised classification algorithm that predicts the probability of an observation belonging to a particular class.

- `LogisticRegression()` creates the model.
- `max_iter=1000` allows sufficient iterations for model optimization.
- `fit()` trains the model using training data.
- `predict()` predicts the classes of testing data.

### Step 8: Evaluate Logistic Regression

```python
lr_accuracy = accuracy_score(y_test, y_pred_lr)
lr_precision = precision_score(y_test, y_pred_lr)
lr_recall = recall_score(y_test, y_pred_lr)
lr_f1 = f1_score(y_test, y_pred_lr)

cm_lr = confusion_matrix(y_test, y_pred_lr)
```

The model is evaluated using five metrics:

1. **Accuracy:** Measures the overall proportion of correct predictions.
2. **Precision:** Measures how many predicted positive cases are actually positive.
3. **Recall:** Measures how many actual positive cases are correctly identified.
4. **F1-Score:** Harmonic mean of Precision and Recall.
5. **Confusion Matrix:** Shows correct and incorrect predictions for each class.

`ConfusionMatrixDisplay.from_predictions()` displays the confusion matrix graphically.

### Step 9: Implement K-Nearest Neighbors (KNN)

```python
knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train_scaled, y_train)

y_pred_knn = knn_model.predict(X_test_scaled)
```

KNN is a supervised classification algorithm that classifies a new data point based on the majority class of its nearest neighbors.

- `KNeighborsClassifier()` creates the KNN model.
- `n_neighbors=5` means the five nearest neighbors are considered.
- `fit()` stores the training data for classification.
- `predict()` predicts the class based on majority voting.

### Step 10: Evaluate KNN

```python
knn_accuracy = accuracy_score(y_test, y_pred_knn)
knn_precision = precision_score(y_test, y_pred_knn)
knn_recall = recall_score(y_test, y_pred_knn)
knn_f1 = f1_score(y_test, y_pred_knn)

cm_knn = confusion_matrix(y_test, y_pred_knn)
```

KNN is evaluated using the same five evaluation metrics as Logistic Regression.

`ConfusionMatrixDisplay.from_predictions()` displays its confusion matrix.

### Step 11: Compare Both Models

A Pandas DataFrame is created to compare the Accuracy, Precision, Recall and F1-Score of both algorithms.

```python
comparison = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
    "Logistic Regression": [
        lr_accuracy, lr_precision, lr_recall, lr_f1
    ],
    "KNN": [
        knn_accuracy, knn_precision, knn_recall, knn_f1
    ]
})

print(comparison)
```

This comparison helps identify which classification algorithm performs better on the testing dataset.

## 4. Result and Analysis

Logistic Regression produced the following results in the provided output:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 80.33% |
| Precision | 76.92% |
| Recall | 90.91% |
| F1-Score | 83.33% |

The Logistic Regression model correctly classified 49 out of 61 testing records.

Its confusion matrix was:

```text
[[19  9]
 [ 3 30]]
```

The KNN model is evaluated separately, and its results are compared with Logistic Regression using the comparison table.

**Analysis:** The comparison of Accuracy, Precision, Recall and F1-Score helps determine the better-performing model. Higher values generally indicate better classification performance, although the importance of each metric depends on the application.

## 5. Important Concepts

| Concept | Meaning |
|---|---|
| Classification | Predicting a category or class |
| Logistic Regression | Classification using predicted probabilities |
| KNN | Classification based on nearest neighbors |
| Training Data | Data used to train the model |
| Testing Data | Data used to evaluate the model |
| Feature Scaling | Bringing features to comparable scales |
| Accuracy | Overall prediction correctness |
| Precision | Correctness of positive predictions |
| Recall | Ability to identify actual positive cases |
| F1-Score | Balance between Precision and Recall |
| Confusion Matrix | Table of actual versus predicted classes |

## 6. Conclusion

Logistic Regression and KNN were successfully implemented for heart disease classification. Data preprocessing, feature scaling and model evaluation were performed. Both algorithms were evaluated using Accuracy, Precision, Recall, F1-Score and Confusion Matrix, and their performances were compared.
