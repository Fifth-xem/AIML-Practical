## 8. Conceptual Understanding and Working of PCA

### 1. What is Dimensionality Reduction?

Dimensionality Reduction is the process of reducing the number of input features in a dataset while preserving as much important information as possible.

For example, our Breast Cancer dataset contains 30 features. Using PCA, we reduce these 30 features to just 2 principal components.

**Advantages:**
- Reduces computational complexity.
- Removes redundant information.
- Helps visualize high-dimensional data.
- Can reduce noise and overfitting in some cases.

### 2. What is Principal Component Analysis (PCA)?

PCA is an unsupervised dimensionality reduction technique used to transform a large number of correlated features into a smaller number of uncorrelated features called Principal Components.

**How PCA works:**

1. Standardizes the dataset so that features have comparable scales.
2. Identifies directions of maximum variance in the data.
3. Creates new principal components from combinations of original features.
4. Arranges components according to the variance they explain.
5. Selects the required number of components.

In our practical, we select 2 principal components from the original 30 features.

### 3. What are Principal Components?

Principal Components are new features created by combining the original input features.

- **PC1 (First Principal Component):** Captures the maximum possible variance.
- **PC2 (Second Principal Component):** Captures the maximum remaining variance and is perpendicular to PC1.

Each subsequent component captures as much remaining variance as possible while being uncorrelated with the previous components.

### 4. What is Explained Variance?

Explained Variance tells us how much information, measured in terms of variance, is retained by each principal component.

In our practical:

| Component | Explained Variance |
|---|---:|
| PC1 | 43.50% |
| PC2 | 19.50% |
| Total | 63.00% |

This means that the two selected principal components retain approximately 63% of the total variance present in the original dataset.

A higher explained variance generally means more information about the original data is retained.

### 5. What is Standardization and Why is it Required?

Standardization converts features to a common scale.

It is important in PCA because features with larger numerical ranges can otherwise dominate the principal components.

Our practical uses `StandardScaler`, which transforms features to approximately:

- Mean = 0
- Standard Deviation = 1

### 6. What is Logistic Regression?

Logistic Regression is a supervised machine learning classification algorithm.

It predicts the probability of an observation belonging to a particular class.

In our practical, it is used twice:

1. Before PCA: Classification using all 30 original features.
2. After PCA: Classification using only 2 principal components.

This allows us to compare the impact of dimensionality reduction on classification performance.

### 7. Evaluation Metrics Used

Our practical uses **Accuracy Score** as the classification evaluation metric.

**Accuracy:**

Accuracy measures the proportion of correctly predicted observations out of all observations.

Formula:

Accuracy = (Correct Predictions / Total Predictions) × 100

In our practical:

| Classification Model | Accuracy |
|---|---:|
| Before PCA (30 features) | 97.37% |
| After PCA (2 features) | 99.12% |

**Interpretation:**

- Before PCA, the model correctly classified approximately 97.37% of test observations.
- After PCA, the model correctly classified approximately 99.12% of test observations.
- Accuracy increased by approximately 1.75 percentage points.

This shows that dimensionality reduction did not reduce classification accuracy in this particular experiment.

**Important:** Accuracy is the only evaluation metric calculated in our current code. Precision, Recall, F1-score and Confusion Matrix are not implemented.

### 8. Other Classification Evaluation Metrics

The following are additional evaluation metrics commonly used in classification problems:

| Metric | Meaning |
|---|---|
| Accuracy | Overall proportion of correct predictions. |
| Precision | Proportion of positive predictions that are actually positive. |
| Recall | Proportion of actual positive cases correctly identified. |
| F1-Score | Harmonic mean of Precision and Recall. |
| Confusion Matrix | Shows correct and incorrect predictions for each class. |

**Note:** These additional metrics are theoretical concepts and are not calculated by our current program.

### 9. What are we Actually Doing in This Practical?

Our practical follows these steps:

1. Load the Breast Cancer dataset containing 30 input features.
2. Divide the dataset into training and testing sets.
3. Standardize the input features.
4. Train Logistic Regression using all 30 features and calculate accuracy.
5. Apply PCA to reduce the features from 30 to 2.
6. Calculate the explained variance of the two principal components.
7. Train another Logistic Regression model using the reduced features.
8. Compare classification accuracy before and after PCA.
9. Generate a two-dimensional scatter plot to visualize the reduced dataset.

### 10. Important Differences

| PCA | Logistic Regression |
|---|---|
| Unsupervised learning technique. | Supervised learning algorithm. |
| Used for dimensionality reduction. | Used for classification. |
| Does not require class labels to find components. | Requires class labels during training. |
| Produces principal components. | Produces class predictions. |

### 11. Advantages and Limitations of PCA

**Advantages:**
- Reduces the number of features.
- Helps visualize complex datasets.
- Reduces computational requirements.
- Can remove redundant information.

**Limitations:**
- Some information may be lost during reduction.
- Principal components can be difficult to interpret.
- Feature standardization is generally important.
- Reduced dimensions do not always improve classification accuracy.

### 12. Final Observation

In this practical, PCA successfully reduced the Breast Cancer dataset from 30 features to 2 principal components while retaining approximately 63% of the total variance.

Logistic Regression accuracy increased from 97.37% to 99.12% after applying PCA.

Thus, the experiment demonstrates how PCA reduces dimensionality, enables visualization of high-dimensional data and affects classification performance.
