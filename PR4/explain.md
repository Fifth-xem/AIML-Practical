
---

# 10. Conceptual Explanation of Data Preprocessing and Exploratory Data Analysis

## 10.1 What are we actually doing in this practical?

In this practical, we are preparing the Heart Disease dataset for machine learning by cleaning, analyzing and transforming the data.

Raw datasets may contain duplicate records, missing values, categorical information and numerical features with different scales. These issues can affect the performance of machine learning algorithms.

Therefore, we perform Data Preprocessing and Exploratory Data Analysis (EDA) before using the data for machine learning.

The main steps are:

1. Load and understand the dataset.
2. Identify and handle missing values.
3. Remove duplicate records.
4. Convert categorical features into numerical form using encoding.
5. Scale numerical features.
6. Perform statistical analysis.
7. Visualize data using histograms and boxplots.
8. Divide the dataset into training and testing sets.

---

## 10.2 Data Preprocessing

Data preprocessing is the process of converting raw data into a clean and suitable format for machine learning.

It includes the following techniques:

### A. Data Cleaning

Data cleaning identifies and removes errors, duplicate records and inconsistencies from the dataset.

In our practical, we use:

```python
df = df.drop_duplicates()
```

This removes repeated records.

Our dataset initially contains 303 records. After removing one duplicate record, 302 records remain.

### B. Missing Value Handling

Missing values are empty or unavailable entries in a dataset.

They can affect statistical calculations and machine learning algorithms.

Common techniques for handling missing values:

- Mean Imputation: Replaces missing numerical values with the average.
- Median Imputation: Replaces missing numerical values with the middle value.
- Mode Imputation: Replaces missing values with the most frequently occurring value.
- Removing Records: Deletes rows or columns containing missing values.

In our practical, we use median imputation:

```python
df['age'] = df['age'].fillna(df['age'].median())
```

Median is preferred when data may contain outliers because it is less affected by extreme values than mean.

**Observation:** Our dataset already contains zero missing values, so the replacement operation does not change any values in the current execution.

### C. Encoding Techniques

Encoding converts categorical data into numerical representations so that machine learning algorithms can process it.

Two common encoding techniques are:

**1. Label Encoding**

Assigns a numerical value to each category.

Example:

| Category | Encoded Value |
|---|---:|
| Male | 0 |
| Female | 1 |

**2. One-Hot Encoding**

Creates separate binary columns for each category.

Example:

| Chest Pain Type | cp_0 | cp_1 | cp_2 | cp_3 |
|---|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 2 | 0 | 0 | 1 | 0 |
| 3 | 0 | 0 | 0 | 1 |

In our practical, we use One-Hot Encoding through:

```python
df = pd.get_dummies(
    df,
    columns=['cp', 'restecg', 'thal'],
    dtype=int
)
```

This converts the selected categorical columns into separate binary columns.

### D. Feature Scaling

Feature scaling is the process of bringing numerical features to a comparable scale.

For example, age may range from 29 to 77, whereas cholesterol may have values in the hundreds.

Features with larger numerical ranges can dominate certain machine learning algorithms.

Two common scaling techniques are:

**1. Min-Max Normalization**

Transforms values into a specified range, usually 0 to 1.

Formula:

X_scaled = (X - X_min) / (X_max - X_min)

**2. Standardization**

Transforms data using mean and standard deviation.

Formula:

Z = (X - Mean) / Standard Deviation

In our practical, we use StandardScaler:

```python
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Standardization produces features with approximately zero mean and unit standard deviation on the training data.

We fit the scaler only on training data and use the same parameters to transform testing data. This prevents data leakage.

---

## 10.3 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is the process of examining a dataset to understand its structure, patterns, distributions and relationships between variables.

It helps identify important characteristics of data before applying machine learning algorithms.

In our practical, EDA is performed using statistical analysis and data visualization.

### A. Statistical Analysis

Statistical analysis helps summarize and understand numerical data.

The following measures are calculated:

**1. Mean**

Mean is the average of all observations.

Mean = Sum of all values / Number of values

In our practical:

```python
df.mean(numeric_only=True)
```

**2. Median**

Median is the middle value when observations are arranged in ascending or descending order.

```python
df.median(numeric_only=True)
```

**3. Standard Deviation**

Standard deviation measures how much the values are spread around the mean.

- Low standard deviation indicates values are closer to the mean.
- High standard deviation indicates greater variation.

```python
df.std(numeric_only=True)
```

**4. Correlation**

Correlation measures the strength and direction of the relationship between two numerical variables.

Its value ranges from -1 to +1.

| Correlation | Meaning |
|---|---|
| +1 | Perfect positive correlation |
| 0 | No linear correlation |
| -1 | Perfect negative correlation |

```python
df.corr(numeric_only=True)
```

**5. Descriptive Statistics**

The `describe()` function provides:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- 50th percentile (median)
- 75th percentile
- Maximum

```python
df.describe()
```

These statistical measures help us understand the distribution and characteristics of the dataset.

### B. Data Visualization

Data visualization represents information graphically to make patterns and distributions easier to understand.

**1. Histogram**

A histogram represents the frequency distribution of numerical data using bars.

In our practical, histograms are created for:

- Age
- Cholesterol

They help us understand how frequently different age and cholesterol values occur.

**2. Boxplot**

A boxplot represents the distribution of numerical data using quartiles.

It displays:

- Minimum (excluding potential outliers)
- First Quartile (Q1)
- Median (Q2)
- Third Quartile (Q3)
- Maximum (excluding potential outliers)
- Potential outliers

The Interquartile Range (IQR) is:

IQR = Q3 - Q1

Potential outliers are commonly identified using:

- Lower Bound = Q1 - 1.5 × IQR
- Upper Bound = Q3 + 1.5 × IQR

In our practical, boxplots are created for age and cholesterol.

They help identify data spread, central tendency and potential outliers.

---

## 10.4 Training and Testing Data

After preprocessing, the dataset is divided into two parts:

**1. Training Dataset**

Used to train a machine learning model so that it can learn patterns from the data.

**2. Testing Dataset**

Used to evaluate the trained model on data it has not seen during training.

In our practical, we use an 80:20 split.

| Dataset | Percentage | Records (approximately) |
|---|---:|---:|
| Training | 80% | 241 |
| Testing | 20% | 61 |
| Total | 100% | 302 |

The `train_test_split()` function performs this division.

The `random_state` parameter ensures reproducibility of the split.

**Important:** This practical only prepares the training and testing datasets. It does not train a classification model or calculate its prediction performance.

---

## 10.5 Evaluation Metrics and Their Importance

Evaluation metrics are measures used to determine how well a machine learning model performs.

Since our dataset contains a target column representing heart disease status, it can be used for a binary classification problem.

However, our current practical does not train a model. Therefore, accuracy, precision, recall, F1-score and confusion matrix are not calculated in this practical.

These metrics are important for evaluating a classification model in a subsequent machine learning task.

### A. Confusion Matrix

A confusion matrix compares actual class labels with predicted class labels.

It contains four important values:

| Term | Meaning |
|---|---|
| True Positive (TP) | Correctly predicted positive cases |
| True Negative (TN) | Correctly predicted negative cases |
| False Positive (FP) | Negative cases incorrectly predicted as positive |
| False Negative (FN) | Positive cases incorrectly predicted as negative |

For heart disease prediction:

- TP: Patient has heart disease and the model predicts heart disease.
- TN: Patient does not have heart disease and the model predicts no heart disease.
- FP: Patient does not have heart disease but the model predicts heart disease.
- FN: Patient has heart disease but the model predicts no heart disease.

### B. Accuracy

Accuracy measures the percentage of correctly predicted observations.

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Higher accuracy indicates that more predictions are correct.

### C. Precision

Precision measures how many predicted positive cases are actually positive.

Precision = TP / (TP + FP)

It is useful when we want to reduce false positive predictions.

### D. Recall

Recall measures how many actual positive cases are correctly identified.

Recall = TP / (TP + FN)

In medical applications, recall is particularly important because missing actual heart disease cases can be dangerous.

### E. F1-Score

F1-score is the harmonic mean of precision and recall.

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

It balances precision and recall and is useful when the dataset has an unequal distribution of classes.

**Note:** These are classification evaluation metrics for a future prediction model, not results produced by the present EDA practical.

---

## 10.6 Overall Workflow of the Practical

The complete workflow can be represented as:

```text
        Heart Disease Dataset
                 |
                 v
         Load Dataset
                 |
                 v
       Explore Dataset Information
                 |
                 v
          Data Cleaning
                 |
                 v
      Missing Value Handling
                 |
                 v
        Remove Duplicates
                 |
                 v
       Categorical Encoding
                 |
                 v
          Feature Scaling
                 |
                 v
        Statistical Analysis
                 |
                 v
        Data Visualization
          /           \
         v             v
     Histograms     Boxplots
          \           /
                 |
                 v
       Training and Testing Split
                 |
                 v
      Dataset Ready for ML Model
```

---

## 10.7 Final Understanding

In this practical, we perform Data Preprocessing and Exploratory Data Analysis on the Heart Disease dataset.

Data preprocessing improves data quality by handling missing values, removing duplicate records, encoding categorical variables and scaling numerical features.

EDA helps us understand the dataset through descriptive statistics, correlation analysis, histograms and boxplots.

Finally, the dataset is divided into training and testing sets so that it can be used for future machine learning model development and evaluation.

**Result:** The Heart Disease dataset is explored, cleaned and prepared for further machine learning applications.

