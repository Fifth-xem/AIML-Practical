---

## 7. Concepts Used in This Practical

### 7.1 What is Classification?

Classification is a supervised machine learning technique used to predict the category or class of given data.

In this practical, we classify patients into two categories based on their medical information:

- `0` – No heart disease
- `1` – Presence of heart disease

We use two classification algorithms: Logistic Regression and K-Nearest Neighbors.

### 7.2 Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for classification problems.

It predicts the probability of an observation belonging to a particular class.

It uses the **Sigmoid Function** to convert the model's output into a probability between 0 and 1.

- If the predicted probability is greater than or equal to 0.5, the output is classified as 1.
- Otherwise, the output is classified as 0.

**In this practical:** Logistic Regression learns patterns from patients' medical information and predicts whether a patient has heart disease.

### 7.3 K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm used for classification.

It classifies a new data point based on the classes of its nearest neighboring data points.

**Working:**

1. Select the value of K.
2. Calculate the distance between the new data point and training data points.
3. Identify the K nearest neighbors.
4. Count the classes of those neighbors.
5. Assign the majority class as the final prediction.

In this practical, we use `K = 5`, meaning the five nearest neighbors are considered for classification.

KNN commonly uses Euclidean Distance to measure the distance between data points.

### 7.4 Data Preprocessing

Data preprocessing is the process of preparing raw data before providing it to a machine learning model.

The following preprocessing operations are performed:

**1. Missing Value Checking**

We use `df.isnull().sum()` to identify missing values in the dataset.

Our dataset contains no missing values, so no replacement is required.

**2. Feature and Target Separation**

- Features (X): The 13 input columns containing patient information.
- Target (y): The `target` column containing the classification result.

**3. Train-Test Split**

The dataset is divided into two parts:

- Training Data (80%): Used to train the machine learning models.
- Testing Data (20%): Used to evaluate the trained models.

We use `random_state=42` to obtain a reproducible split and `stratify=y` to maintain the class distribution in both sets.

**4. Feature Scaling**

We use StandardScaler to standardize the input features.

It transforms features so that they have approximately zero mean and unit standard deviation.

This is particularly important for KNN because it calculates distances between data points. Without scaling, features with larger numerical values could dominate the distance calculation.

We fit the scaler only on training data and apply the same transformation to testing data to avoid data leakage.

---

## 8. Model Evaluation Metrics

After training both classification models, we evaluate their performance using five evaluation metrics.

### 8.1 Confusion Matrix

A Confusion Matrix is a table used to compare actual class labels with predicted class labels.

It contains four important values:

| Term | Meaning |
|---|---|
| True Positive (TP) | Model correctly predicts the positive class (1). |
| True Negative (TN) | Model correctly predicts the negative class (0). |
| False Positive (FP) | Model predicts 1, but the actual class is 0. |
| False Negative (FN) | Model predicts 0, but the actual class is 1. |

For binary classification, the confusion matrix is arranged as:

```text
                 Predicted
                0       1

Actual  0      TN      FP
        1      FN      TP
```

**Confusion Matrix of Logistic Regression:**

```text
[[19  9]
 [ 3 30]]
```

Interpretation:

- TN = 19
- FP = 9
- FN = 3
- TP = 30

This means the model correctly classified 19 patients without heart disease and 30 patients with heart disease.

### 8.2 Accuracy

Accuracy measures the percentage of total predictions that are correct.

**Formula:**

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Higher accuracy indicates that the model makes more correct predictions overall.

### 8.3 Precision

Precision measures how many of the observations predicted as positive are actually positive.

**Formula:**

Precision = TP / (TP + FP)

Higher precision means fewer false positive predictions.

### 8.4 Recall

Recall measures how many actual positive observations are correctly identified by the model.

**Formula:**

Recall = TP / (TP + FN)

Higher recall means fewer actual positive cases are missed.

### 8.5 F1-Score

F1-Score is the harmonic mean of Precision and Recall.

It provides a balance between Precision and Recall.

**Formula:**

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

A higher F1-Score indicates a better balance between Precision and Recall.

### 8.6 Evaluation Results of Logistic Regression

The Logistic Regression model produced the following results:

| Metric | Result |
|---|---:|
| Accuracy | 80.33% |
| Precision | 76.92% |
| Recall | 90.91% |
| F1-Score | 83.33% |

These values indicate that Logistic Regression correctly classified 49 out of 61 testing records.

---

## 9. Comparison of Logistic Regression and KNN

Both algorithms are trained using the same training dataset and evaluated using the same testing dataset.

The comparison is performed using:

- Accuracy
- Precision
- Recall
- F1-Score

The comparison table generated by the program helps identify which algorithm performs better.

**Important observations:**

- Accuracy indicates overall prediction correctness.
- Precision indicates the reliability of positive predictions.
- Recall indicates the ability to identify actual positive cases.
- F1-Score balances Precision and Recall.

The algorithm with higher scores is generally considered better for the corresponding evaluation metric. The final choice depends on the application and the importance of different types of prediction errors.

## 10. Overall Working of the Practical

The complete workflow followed in this practical is:

```text
Heart Disease Dataset
        |
        v
   Data Loading
        |
        v
 Missing Value Checking
        |
        v
 Feature and Target Separation
        |
        v
   Train-Test Split
        |
        v
    Feature Scaling
        |
        v
  ---------------------
  |                   |
  v                   v
Logistic Regression   KNN
  |                   |
  v                   v
Predictions          Predictions
  |                   |
  v                   v
Model Evaluation     Model Evaluation
  |                   |
  ---------------------
          |
          v
   Compare Both Models
          |
          v
     Final Analysis
```

## 11. Conclusion

In this practical, Logistic Regression and K-Nearest Neighbors algorithms are implemented for binary classification using the Heart Disease dataset. Data preprocessing and feature scaling are performed before model training. Both models are evaluated using Accuracy, Precision, Recall, F1-Score and Confusion Matrix. Their results are compared to understand their classification performance.
