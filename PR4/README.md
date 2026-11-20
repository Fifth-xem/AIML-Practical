
# AIML Practical No. 4 – Data Preprocessing and Exploratory Data Analysis (EDA)

## 1. Practical Title

**Data Preprocessing and Exploratory Data Analysis:**

Download a standard dataset (Heart Disease, Diabetes or Titanic dataset) and perform:
- Data cleaning
- Missing value handling
- Feature scaling
- Encoding techniques
- Statistical analysis
- Data visualization using histograms and boxplots
- Split the dataset into training and testing sets.

---

## 2. Dataset Information

**Dataset Used:** Heart Disease Dataset

**Dataset Details:**

| Property | Value |
|---|---|
| Dataset Name | Heart Disease |
| Initial Records | 303 |
| Total Columns | 14 |
| Input Features | 13 |
| Target Column | target |
| Data Types | int64 and float64 |

**Important Columns:**

| Column | Description |
|---|---|
| age | Age of patient |
| sex | Sex category |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Cholesterol level |
| fbs | Fasting blood sugar |
| restecg | Resting ECG results |
| thalach | Maximum heart rate |
| exang | Exercise-induced angina |
| oldpeak | ST depression |
| slope | Slope of ST segment |
| ca | Number of major vessels |
| thal | Thalassemia category |
| target | Heart disease target |

### How is the dataset accessed?

The dataset is accessed using Pandas:

```python
df = pd.read_csv("D:/AIML Practicle/PR 4/heart.csv")
```

- `pd.read_csv()` reads a CSV file.
- The given path specifies the location of the dataset.
- `df` stores the dataset as a Pandas DataFrame.

**Important:** The dataset is stored locally. It is not downloaded automatically by the code.

### Required Folder Structure

Keep the Python file and CSV file in the same directory:

```text
PR4/
│
├── AIML_PR4.py
├── heart.csv
└── README.md
```

For this arrangement, use:

```python
df = pd.read_csv("heart.csv")
```

The dataset does not have to be in the same directory if an appropriate absolute or relative path is provided.

---

## 3. Code Explanation

### A. Importing Required Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as s

sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")
```

**Explanation:**

| Library | Purpose |
|---|---|
| Pandas | Loading, cleaning and manipulating datasets |
| Matplotlib | Creating graphs and visualizations |
| Seaborn | Creating statistical visualizations |
| NumPy | Numerical operations |
| Statistics | Calculating statistical values such as mean |

- `sns.set_style()` sets the Seaborn graph style.
- `plt.style.use()` sets the Matplotlib graph style.

Note: NumPy is imported but not directly used in the original code.

### B. Loading the Dataset

```python
df = pd.read_csv("heart.csv")
df.head()
```

**Explanation:**

- `read_csv()` reads the CSV dataset.
- `df` stores the dataset in DataFrame format.
- `head()` displays the first five rows by default.

### C. Understanding the Dataset

```python
df.info()

print(df.columns)
print(df.dtypes)
print(df.dtypes.value_counts())

print(df.describe())
print(df.head())
```

| Function | Purpose |
|---|---|
| `df.info()` | Displays dataset information, rows, columns and data types |
| `df.columns` | Displays column names |
| `df.dtypes` | Displays data types of columns |
| `df.dtypes.value_counts()` | Counts columns according to data type |
| `df.describe()` | Generates statistical summary |
| `df.head()` | Displays first five records |

### D. Checking Dataset Size and Missing Values

```python
n = df.columns[df.dtypes != 'object']

size = df.size
shape = df.shape

print("Size:", size)
print("Shape:", shape)

print(df.isnull().sum())
```

**Explanation:**

- `df.size` returns the total number of elements.
- `df.shape` returns the number of rows and columns.
- `df.isnull().sum()` counts missing values in each column.
- `n` stores the names of numerical columns.

For the original dataset:

- Total elements = 303 × 14 = 4242.
- Shape = (303, 14).

### E. Missing Value Handling

```python
df['age'] = df['age'].fillna(df['age'].median())

print(df.isnull().sum())
```

**Explanation:**

- `median()` calculates the median age.
- `fillna()` replaces missing age values with the median.
- `isnull().sum()` checks missing values again.

**Why use median?**

Median is less affected by extreme values and outliers than mean, making it useful for replacing missing numerical values.

In this dataset, all columns already have zero missing values, so no actual replacement is required.

### F. Removing Duplicate Records

```python
df = df.drop_duplicates()

print(df.shape)
```

**Explanation:**

- `drop_duplicates()` removes duplicate rows.
- The dataset initially contains 303 records.
- After removing duplicates, 302 records remain.

### G. Statistical Analysis

```python
print(df.describe())

print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.std(numeric_only=True))
print(df.corr(numeric_only=True))
```

| Function | Purpose |
|---|---|
| `describe()` | Statistical summary |
| `mean()` | Calculates average |
| `median()` | Calculates middle value |
| `std()` | Calculates standard deviation |
| `corr()` | Calculates correlation between columns |

**Correlation:** Measures the strength and direction of the relationship between two variables. Its value ranges from -1 to +1.

### H. Data Visualization – Histograms

**Histogram of Age:**

```python
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=20, edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

**Histogram of Cholesterol:**

```python
plt.figure(figsize=(8, 5))
plt.hist(df['chol'], bins=15, edgecolor='black')
plt.title('Histogram of Cholesterol')
plt.xlabel('Cholesterol')
plt.ylabel('Frequency')
plt.show()
```

**Explanation:**

- `plt.figure()` creates a plotting area.
- `plt.hist()` creates a histogram.
- `bins` specifies the number of intervals.
- `xlabel()` and `ylabel()` label the axes.
- `show()` displays the graph.

**Purpose:** Histograms display the frequency distribution of numerical data.

### I. Data Visualization – Boxplots

**Boxplot of Age:**

```python
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['age'])
plt.title('Boxplot of Age')
plt.show()
```

**Boxplot of Cholesterol:**

```python
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['chol'])
plt.title('Boxplot of Cholesterol')
plt.show()
```

**Explanation:**

A boxplot displays:
- Median
- First quartile (Q1)
- Third quartile (Q3)
- Interquartile Range (IQR)
- Potential outliers

**Purpose:** Boxplots help understand data distribution, spread and potential outliers.

### J. Calculating Average Age

```python
average = s.mean(df['age'])
print("Average age:", average)
```

**Explanation:**

- `s.mean()` calculates the average age using Python's Statistics library.
- The result is displayed using `print()`.

### K. Extracting Particular Columns

```python
print(df['age'])
print(df['sex'])
print(df['trestbps'])
print(df['chol'])
```

**Explanation:**

These statements display individual columns from the dataset.

- `age`: Patient age.
- `sex`: Sex category.
- `trestbps`: Resting blood pressure.
- `chol`: Cholesterol level.

### L. Splitting Dataset into Training and Testing Sets

```python
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=56
)

print(X_train)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
```

**Explanation:**

| Variable | Meaning |
|---|---|
| X | Independent features |
| y | Dependent target variable |
| X_train | Training features |
| X_test | Testing features |
| y_train | Training target |
| y_test | Testing target |

**Important Parameters:**

- `drop('target', axis=1)` removes the target column from input features.
- `test_size=0.2` allocates 20% data for testing and 80% for training.
- `random_state=56` ensures reproducible splitting.

**Dataset Split:**

| Dataset | Records |
|---|---:|
| Training Data | 241 |
| Testing Data | 61 |
| Total | 302 |

---

## 4. Additional Techniques Required by the Practical Title

The original code does not explicitly implement encoding and feature scaling. Add the following sections to cover these requirements.

### A. Encoding Techniques – One-Hot Encoding

```python
df = pd.get_dummies(
    df,
    columns=['cp', 'restecg', 'thal'],
    dtype=int
)
```

**Explanation:**

- One-Hot Encoding converts categorical values into separate binary columns.
- For example, the `cp` column is converted into `cp_0`, `cp_1`, `cp_2` and `cp_3`.
- This makes categorical information suitable for machine learning algorithms.

Add this after duplicate removal and before statistical analysis.

### B. Feature Scaling – StandardScaler

Import:

```python
from sklearn.preprocessing import StandardScaler
```

After splitting the dataset:

```python
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

**Explanation:**

- StandardScaler standardizes numerical features.
- `fit_transform()` calculates scaling parameters from training data and scales it.
- `transform()` applies the same parameters to testing data.
- This prevents data leakage from the testing set.

---

## 5. Ubuntu Installation and Execution

### Step 1: Check Python and pip

```bash
python3 --version
pip3 --version
```

### Step 2: Install Python and Virtual Environment

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 3: Create and Activate Virtual Environment

```bash
python3 -m venv aiml_env
source aiml_env/bin/activate
```

### Step 4: Install Required Libraries

```bash
python3 -m pip install pandas numpy matplotlib seaborn scikit-learn
```

### Step 5: Verify Installation

```bash
python3 -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('All libraries installed successfully')"
```

### Step 6: Run the Program

Keep the Python file and dataset in the same folder.

```text
PR4/
│
├── AIML_PR4.py
└── heart.csv
```

Change the dataset path in the code to:

```python
df = pd.read_csv("heart.csv")
```

Execute:

```bash
cd ~/PR4
python3 AIML_PR4.py
```

**Note:** If using an older Ubuntu system with Python 3.4, modern package versions may not be compatible. Older compatible package versions or a newer Python installation may be required.

---

## 6. Offline Execution – Is Internet Required?

**The practical can run completely offline after installing the required dependencies and obtaining the dataset.**

| Operation | Internet Required? |
|---|---|
| Importing installed libraries | No |
| Reading heart.csv | No |
| Data cleaning | No |
| Missing value handling | No |
| Encoding | No |
| Feature scaling | No |
| Statistical analysis | No |
| Histograms and boxplots | No |
| Training/testing split | No |

The code uses:

```python
pd.read_csv("heart.csv")
```

This reads a locally stored CSV file. It does not download the dataset from the internet or use Scikit-learn's dataset-fetching functions.

**What should be carried to college?**

- AIML_PR4.py – Python program.
- heart.csv – Dataset.
- Required Python libraries installed on the college system.

Internet is only needed if dependencies must be downloaded and are not already available. Alternatively, dependencies can be installed from previously downloaded offline packages.

---

## 7. Important Viva Questions and Answers

**Q1. What is Data Preprocessing?**

Data preprocessing is the process of cleaning and transforming raw data into a suitable format for machine learning.

**Q2. What is Exploratory Data Analysis (EDA)?**

EDA is the process of analyzing and understanding a dataset using statistical methods and visualizations.

**Q3. Which dataset is used in this practical?**

Heart Disease dataset.

**Q4. What is a DataFrame?**

A DataFrame is a two-dimensional tabular data structure provided by Pandas.

**Q5. What is the purpose of `head()`?**

It displays the first five rows of a dataset by default.

**Q6. What is the purpose of `info()`?**

It displays information about rows, columns, data types and non-null values.

**Q7. What is `describe()`?**

It generates a statistical summary of numerical columns.

**Q8. What is the difference between `isnull()` and `dropna()`?**

`isnull()` identifies missing values, whereas `dropna()` removes rows or columns containing missing values.

**Q9. Why is median used for missing value handling?**

Median is less affected by extreme values and outliers than mean.

**Q10. What is `drop_duplicates()`?**

It removes duplicate records from a dataset.

**Q11. What is Encoding?**

Encoding converts categorical data into numerical representations.

**Q12. What is One-Hot Encoding?**

It converts categories into separate binary columns.

**Q13. What is Feature Scaling?**

Feature scaling brings numerical features into a comparable range.

**Q14. What is StandardScaler?**

StandardScaler standardizes features using their mean and standard deviation.

**Q15. What is a histogram?**

A histogram is a graph that represents the frequency distribution of numerical data.

**Q16. What is a boxplot?**

A boxplot represents the median, quartiles, spread and potential outliers.

**Q17. What is the Interquartile Range (IQR)?**

IQR is the difference between the third quartile and first quartile.

IQR = Q3 - Q1

**Q18. What is correlation?**

Correlation measures the strength and direction of the relationship between two variables.

**Q19. What is the purpose of `train_test_split()`?**

It divides the dataset into training and testing sets.

**Q20. What is the purpose of `random_state`?**

It ensures that the random splitting produces reproducible results.

**Q21. What is the difference between training and testing data?**

Training data is used to train a model, while testing data is used to evaluate its performance on unseen data.

**Q22. Why do we use Pandas?**

Pandas is used for loading, organizing, cleaning and manipulating datasets.

**Q23. Does this practical require internet during execution?**

No. It runs offline if the dataset and required libraries are already available locally.

**Q24. How many records remain after removing duplicates?**

302 records remain from the original 303 records.

**Q25. What is the target column?**

The `target` column represents the heart disease outcome and is used as the dependent variable.

---

## 8. Important Functions to Remember

| Function | Purpose |
|---|---|
| `pd.read_csv()` | Load CSV dataset |
| `df.head()` | Display first five rows |
| `df.info()` | Display dataset information |
| `df.describe()` | Statistical summary |
| `df.shape` | Rows and columns |
| `df.size` | Total elements |
| `df.isnull().sum()` | Count missing values |
| `fillna()` | Handle missing values |
| `drop_duplicates()` | Remove duplicate rows |
| `mean()` | Calculate mean |
| `median()` | Calculate median |
| `std()` | Calculate standard deviation |
| `corr()` | Calculate correlation |
| `plt.hist()` | Create histogram |
| `sns.boxplot()` | Create boxplot |
| `pd.get_dummies()` | Perform One-Hot Encoding |
| `StandardScaler()` | Perform feature scaling |
| `train_test_split()` | Split training and testing data |

---

## 9. Final Practical Summary

In this practical, the Heart Disease dataset is loaded using Pandas. Dataset information is explored using functions such as `info()`, `describe()` and `shape`.

Data cleaning is performed by checking missing values, replacing missing age values with the median and removing duplicate records.

Statistical analysis is performed using mean, median, standard deviation and correlation. Histograms and boxplots are created to visualize age and cholesterol distributions.

One-Hot Encoding and StandardScaler can be added to perform categorical encoding and feature scaling. Finally, the dataset is divided into 80% training data and 20% testing data.

**Result:** Data preprocessing and exploratory data analysis are performed on the Heart Disease dataset, and the dataset is prepared for further machine learning tasks.

