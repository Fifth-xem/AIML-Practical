---

# 9. Important Concepts Used in This Practical

## 9.1 Advanced Machine Learning

Advanced Machine Learning involves using algorithms and techniques to improve the learning and prediction capabilities of machine learning models.

In this practical, three classification algorithms are implemented and compared:

- Support Vector Machine (SVM)
- Random Forest
- AdaBoost

The objective is to understand how these algorithms classify data and how their performance can be improved through hyperparameter optimization.

## 9.2 Classification

Classification is a supervised machine learning technique in which a model learns from labelled training data and predicts the category of new data.

In this practical, the Breast Cancer Wisconsin dataset is used to classify tumors into two categories:

- Malignant (cancerous)
- Benign (non-cancerous)

The model learns patterns from the input features and predicts the corresponding class.

## 9.3 Support Vector Machine (SVM)

SVM is a supervised machine learning algorithm used for classification.

It finds an optimal separating boundary called a **hyperplane** between different classes.

Its main objective is to maximize the margin, which is the distance between the hyperplane and the nearest data points of each class.

Important concepts:

- Hyperplane: The decision boundary separating classes.
- Margin: The distance between the hyperplane and the nearest data points.
- Kernel: A function used to handle data that cannot be separated easily using a straight line.
- C: A regularization parameter that controls the penalty for classification errors.

In this practical, SVM is implemented using `SVC()` and its C and kernel parameters are optimized using Grid Search.

## 9.4 Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions.

Each decision tree produces a prediction, and the final classification is determined through majority voting.

Important concepts:

- Decision Tree: A tree-like model that makes decisions based on input features.
- Ensemble Learning: Combining multiple models to obtain a stronger prediction.
- n_estimators: Number of decision trees in the forest.
- max_depth: Maximum depth allowed for each decision tree.

Random Forest generally provides good performance and reduces the risk of overfitting compared with relying on a single decision tree.

## 9.5 AdaBoost (Adaptive Boosting)

AdaBoost is an ensemble learning technique that combines multiple weak learners to create a stronger model.

It trains learners sequentially. After each training stage, more attention is given to incorrectly classified samples so that subsequent learners can improve their predictions.

Important concepts:

- Weak Learner: A simple model that performs slightly better than random guessing.
- Boosting: Combining weak learners sequentially to create a strong learner.
- n_estimators: Number of weak learners used.
- learning_rate: Controls the contribution of each learner.

In this practical, AdaBoost is implemented using `AdaBoostClassifier()`.

## 9.6 Data Splitting

Before training a machine learning model, the dataset is divided into training and testing sets.

In this practical:

- Training data: 80%
- Testing data: 20%

**Training Set:** Used by the model to learn patterns from the dataset.

**Testing Set:** Used to evaluate how well the trained model predicts unseen data.

The `random_state` parameter ensures reproducible splitting, while `stratify=y` maintains the class distribution in both sets.

## 9.7 Feature Scaling and Standardization

Feature scaling is the process of bringing numerical features to a comparable scale.

SVM is sensitive to feature magnitudes. Features with larger numerical values can influence the model more strongly.

StandardScaler transforms features using:

\[
z = \frac{x-\mu}{\sigma}
\]

Where:

- x = Original feature value
- μ = Mean of the feature
- σ = Standard deviation of the feature
- z = Standardized value

In this practical, `StandardScaler()` is used before SVM through a Pipeline.

Random Forest and AdaBoost do not generally require feature scaling because they are tree-based algorithms.

## 9.8 Cross-Validation

Cross-validation is a technique used to evaluate how well a machine learning model performs on different subsets of training data.

In this practical, **5-Fold Cross-Validation** is used.

Working:

1. The training dataset is divided into five equal folds.
2. Four folds are used for training.
3. One fold is used for validation.
4. The process is repeated five times, changing the validation fold each time.
5. The average accuracy of all five iterations is calculated.

Cross-validation helps provide a more reliable estimate of model performance than relying on a single validation split.

In the program, it is implemented using:

```python
GridSearchCV(cv=5)
```

## 9.9 Hyperparameter Tuning

Hyperparameters are settings that control how a machine learning algorithm learns.

They are selected before or during model training rather than learned directly from the training data.

Examples used in this practical:

| Algorithm | Hyperparameters |
|---|---|
| SVM | C, kernel |
| Random Forest | n_estimators, max_depth |
| AdaBoost | n_estimators, learning_rate |

Hyperparameter tuning means testing different combinations of these settings to find the combination that gives the best model performance.

## 9.10 Grid Search

Grid Search is a hyperparameter optimization technique that tests all specified combinations of hyperparameter values.

In this practical, `GridSearchCV()` is used.

Working:

1. Different hyperparameter combinations are defined.
2. Each combination is evaluated using 5-Fold Cross-Validation.
3. The average accuracy is calculated for each combination.
4. The combination with the highest average accuracy is selected.
5. The best model is used for final testing.

Important attributes:

- `best_params_`: Returns the best hyperparameter combination.
- `best_score_`: Returns the highest average cross-validation score.
- `best_estimator_`: Returns the model with the best parameters.

**Difference between Parameters and Hyperparameters:**

Parameters are learned by the model during training, whereas hyperparameters are settings that control the learning process.

## 9.11 Model Optimization

Model optimization is the process of improving a machine learning model by selecting suitable hyperparameters and configurations.

In this practical, model optimization is performed using Grid Search with 5-Fold Cross-Validation.

Two performance evaluations are performed:

**Before Optimization:**

- The model is trained using its default settings.
- Predictions are generated on the testing dataset.
- Accuracy, precision, recall and F1-score are calculated.

**After Optimization:**

- Grid Search identifies the best hyperparameters.
- The optimized model is used to make predictions on the same testing dataset.
- The same evaluation metrics are calculated again.

The results are compared to understand the effect of optimization.

Note: Optimization does not guarantee that every evaluation metric will improve. Sometimes the optimized model produces the same predictions as the original model.

---

# 10. Model Evaluation Metrics

Evaluation metrics are used to measure how accurately a machine learning model performs classification.

In this practical, four evaluation metrics are used.

## 10.1 Confusion Matrix

A Confusion Matrix is a table used to evaluate classification performance by comparing actual values with predicted values.

It contains four important terms:

| Term | Meaning |
|---|---|
| True Positive (TP) | Model correctly predicts a positive class. |
| True Negative (TN) | Model correctly predicts a negative class. |
| False Positive (FP) | Model incorrectly predicts positive when actual class is negative. |
| False Negative (FN) | Model incorrectly predicts negative when actual class is positive. |

For this practical, Scikit-learn considers class 1 (Benign) as the positive class by default.

The confusion matrix is not explicitly printed in the current program, but its concepts help explain the evaluation metrics.

## 10.2 Accuracy

Accuracy measures the percentage of total predictions that are correct.

Formula:

\[
Accuracy = \frac{TP+TN}{TP+TN+FP+FN}
\]

It indicates the overall correctness of the model.

In the practical, `accuracy_score()` is used to calculate accuracy.

## 10.3 Precision

Precision measures how many samples predicted as positive are actually positive.

Formula:

\[
Precision = \frac{TP}{TP+FP}
\]

Higher precision means fewer false positive predictions.

In the practical, `precision_score()` is used.

## 10.4 Recall

Recall measures how many actual positive samples are correctly identified by the model.

Formula:

\[
Recall = \frac{TP}{TP+FN}
\]

Higher recall means fewer false negative predictions.

In the practical, `recall_score()` is used.

## 10.5 F1-Score

F1-score is the harmonic mean of precision and recall.

Formula:

\[
F1 = 2 \times \frac{Precision \times Recall}{Precision+Recall}
\]

It provides a balance between precision and recall.

A higher F1-score indicates a better balance between these two metrics.

In the practical, `f1_score()` is used.

## 10.6 Why Are Multiple Evaluation Metrics Used?

Accuracy alone may not provide a complete understanding of classification performance, especially when the dataset contains unequal class distributions.

Therefore:

- Accuracy measures overall correctness.
- Precision measures the correctness of positive predictions.
- Recall measures the ability to identify actual positive samples.
- F1-score balances precision and recall.

Using all four metrics provides a better understanding of model performance.

---

# 11. Comparison of Models

The practical compares three machine learning algorithms:

| Feature | SVM | Random Forest | AdaBoost |
|---|---|---|---|
| Learning type | Supervised | Supervised | Supervised |
| Algorithm type | Classification | Ensemble | Ensemble |
| Main working principle | Maximum-margin hyperplane | Multiple decision trees and voting | Sequential boosting |
| Feature scaling | Generally required | Not required | Not generally required |
| Optimization | C, kernel | n_estimators, max_depth | n_estimators, learning_rate |

## 12. Why Is Model Comparison Important?

Different machine learning algorithms learn patterns differently.

Comparing SVM, Random Forest and AdaBoost helps us:

- Understand the strengths of different algorithms.
- Identify which model performs better on the given dataset.
- Evaluate the effect of hyperparameter tuning.
- Select a suitable model based on evaluation metrics.

The model with the highest accuracy is not automatically the best choice for every problem. Precision, recall and F1-score should also be considered.

## 13. Important Difference Between Cross-Validation Accuracy and Test Accuracy

These two values are not the same.

**Cross-Validation Accuracy:**

- Calculated using five validation folds from the training dataset.
- Used by Grid Search to select the best hyperparameters.
- Stored in `grid.best_score_`.

**Test Accuracy:**

- Calculated using the separate testing dataset.
- Measures the performance of the final model on unseen data.
- Calculated using `accuracy_score()`.

Both values are important because cross-validation helps select the model, while test accuracy evaluates its final generalization performance.

---

# 14. Overall Working of the Practical

The complete workflow is:

1. Load the Breast Cancer Wisconsin dataset.
2. Separate input features and target labels.
3. Divide the dataset into training and testing sets.
4. Define SVM, Random Forest and AdaBoost.
5. Train and evaluate the models using default hyperparameters.
6. Apply 5-Fold Cross-Validation.
7. Perform hyperparameter tuning using Grid Search.
8. Select the best model for each algorithm.
9. Evaluate optimized models on the testing dataset.
10. Compare performance before and after optimization.

**Final Outcome:** The practical demonstrates how different machine learning classification algorithms can be implemented, optimized and compared using cross-validation, Grid Search and evaluation metrics.
