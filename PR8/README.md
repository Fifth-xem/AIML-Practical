# Practical No. 8: Dimensionality Reduction using Principal Component Analysis (PCA)

## 1. Aim

To apply Principal Component Analysis (PCA) on a high-dimensional dataset and compare:
- Number of features before and after PCA.
- Visualization of reduced dimensions.
- Classification performance before and after PCA.

## 2. Dataset Used

**Breast Cancer Wisconsin Diagnostic Dataset**

- Source: Scikit-learn built-in dataset.
- Total features: 30.
- Target classes: Malignant and Benign.
- Dataset type: Classification dataset.

The dataset contains measurements of cell nuclei used to classify breast tumors.

### Dataset Loading

```python
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X = data.data
y = data.target
```

- `load_breast_cancer()` loads the built-in dataset.
- `X` contains input features.
- `y` contains target class labels.

No separate CSV file is required when using this method.

## 3. Explanation of the Code

### A. Importing Libraries

```python
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
```

- **Matplotlib:** Used for plotting graphs.
- **Scikit-learn:** Provides machine learning algorithms and preprocessing tools.
- **train_test_split:** Divides the dataset into training and testing sets.
- **StandardScaler:** Standardizes the features.
- **PCA:** Performs dimensionality reduction.
- **LogisticRegression:** Performs classification.
- **accuracy_score:** Calculates classification accuracy.

### B. Loading the Dataset

```python
data = load_breast_cancer()

X = data.data
y = data.target

print("Original number of features:", X.shape[1])
```

The Breast Cancer dataset is loaded directly from Scikit-learn.

`X` stores the 30 input features, while `y` stores the class labels.

`X.shape[1]` gives the number of input features.

### C. Splitting the Dataset

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The dataset is divided into:
- 80% training data.
- 20% testing data.

`random_state=42` ensures that the same split is obtained when the program runs again.

### D. Feature Standardization

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Standardization brings features to a comparable scale, generally with mean 0 and standard deviation 1.

It is important because PCA is affected by differences in feature scales.

`fit_transform()` learns scaling parameters from training data and transforms it. `transform()` applies the same parameters to testing data.

### E. Classification Before PCA

```python
model1 = LogisticRegression(max_iter=5000)

model1.fit(X_train_scaled, y_train)

y_pred1 = model1.predict(X_test_scaled)

accuracy_before = accuracy_score(y_test, y_pred1)
```

Logistic Regression is trained using all 30 original features.

The model predicts the test data, and `accuracy_score()` calculates its classification accuracy.

This gives the baseline performance before applying PCA.

### F. Applying PCA

```python
pca = PCA(n_components=2)

X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
```

PCA converts the original 30 features into 2 new features called Principal Components.

- PC1: First Principal Component.
- PC2: Second Principal Component.

These components retain as much data variance as possible for the selected number of components.

```python
print("Number of features after PCA:", X_train_pca.shape[1])

print("Explained variance:", pca.explained_variance_ratio_)

print("Total explained variance:", sum(pca.explained_variance_ratio_))
```

- `explained_variance_ratio_` shows the proportion of variance explained by each component.
- Total explained variance gives the combined variance retained by both components.

### G. Classification After PCA

```python
model2 = LogisticRegression(max_iter=5000)

model2.fit(X_train_pca, y_train)

y_pred2 = model2.predict(X_test_pca)

accuracy_after = accuracy_score(y_test, y_pred2)
```

A second Logistic Regression model is trained using the 2 reduced features.

Its accuracy is calculated and compared with the accuracy before PCA to understand the impact of dimensionality reduction.

### H. PCA Visualization

```python
plt.figure(figsize=(8, 6))

plt.scatter(
    X_train_pca[:, 0],
    X_train_pca[:, 1],
    c=y_train
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - 2D Visualization")

plt.show()
```

A scatter plot is generated using the first two principal components.

- X-axis represents PC1.
- Y-axis represents PC2.
- Different colors represent different target classes.

This helps visualize how the two classes are distributed in the reduced-dimensional space.

## 4. Results and Observations

| Parameter | Before PCA | After PCA |
|---|---:|---:|
| Number of features | 30 | 2 |
| Classification accuracy | 97.37% | 99.12% |

### Explained Variance

- PC1 explains approximately 43.50% of the variance.
- PC2 explains approximately 19.50% of the variance.
- Combined explained variance is approximately 63%.

### Observations

1. PCA reduced the number of features from 30 to 2.
2. Approximately 93.33% of the original feature count was eliminated.
3. The two principal components retained approximately 63% of the total variance.
4. Classification accuracy increased from approximately 97.37% to 99.12% in this experiment.
5. PCA made it possible to visualize the high-dimensional data in two dimensions.

## 5. Important Concepts

**Dimensionality Reduction:** The process of reducing the number of input features while retaining important information.

**PCA:** An unsupervised dimensionality reduction technique that transforms correlated features into a smaller set of uncorrelated variables called principal components.

**Principal Components:** New features formed as combinations of the original features. They are arranged according to the amount of variance they explain.

**Explained Variance:** Measures how much information, in terms of data variance, is retained by each principal component.

**Standardization:** A preprocessing technique that brings features to a comparable scale.

**Logistic Regression:** A supervised classification algorithm used to predict class labels.

## 6. Dependencies and Execution Commands

Install the required libraries:

```bash
sudo apt update

sudo apt install python3 python3-pip python3-venv -y

python3 -m venv pca_env

source pca_env/bin/activate

python -m pip install --upgrade pip

python -m pip install numpy matplotlib scikit-learn
```

Run the program:

```bash
python3 pca.py
```

Replace `pca.py` with your actual Python filename if different.

## 7. Conclusion

PCA was successfully applied to the Breast Cancer dataset to reduce its dimensionality from 30 features to 2 principal components. The reduced data was visualized using a scatter plot, and Logistic Regression classification performance was compared before and after PCA. The experiment demonstrated dimensionality reduction and its impact on classification performance.
