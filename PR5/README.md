# AIML Practical No. 5 – Regression Techniques

## 1. Aim

To implement and compare Linear Regression and Polynomial Regression using the California Housing dataset. Evaluate both models using Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score.

## 2. Dataset Used

**California Housing Dataset**

- Source: Scikit-learn.
- Total records: 20,640.
- Input features: 8.
- Target variable: `MedHouseVal` (Median House Value).
- Total columns: 9.

The dataset contains information such as median income, house age, average rooms, population, latitude and longitude.

**Dataset Access Method:**

Originally, the program uses:

```python
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame
```

Scikit-learn downloads the dataset automatically if it is not already cached. No manually downloaded CSV is required with this method.

## 3. Explanation of the Code

### Step 1: Import Required Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
```

- **Pandas:** Handles dataset and comparison tables.
- **NumPy:** Performs numerical operations for graphs.
- **Matplotlib:** Creates graphs.
- **Scikit-learn:** Provides regression algorithms, preprocessing and evaluation metrics.

### Step 2: Load the Dataset

```python
data = fetch_california_housing(as_frame=True)
df = data.frame
```

Loads the California Housing dataset into a Pandas DataFrame.

`df.head()` displays the first five records, and `df.shape` displays the dataset dimensions.

### Step 3: Separate Features and Target

```python
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]
```

- `X` contains the eight independent input features.
- `y` contains the dependent variable (house value) that we want to predict.

### Step 4: Split the Dataset

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)
```

Divides the dataset into:

- 80% training data.
- 20% testing data.

`random_state=42` ensures that the same split is obtained when the program is executed again.

### Step 5: Linear Regression

```python
linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

linear_prediction = linear_model.predict(X_test)
```

Linear Regression finds a straight-line relationship between input features and the target variable.

- `LinearRegression()` creates the model.
- `fit()` trains the model.
- `predict()` predicts house values using testing data.

### Step 6: Evaluate Linear Regression

```python
linear_mse = mean_squared_error(y_test, linear_prediction)
linear_mae = mean_absolute_error(y_test, linear_prediction)
linear_r2 = r2_score(y_test, linear_prediction)
```

Calculates three performance metrics:

- **MSE:** Mean Squared Error; measures the average squared prediction error. Lower is better.
- **MAE:** Mean Absolute Error; measures the average absolute prediction error. Lower is better.
- **R² Score:** Measures how well the model explains variations in the target variable. Higher is better.

### Step 7: Polynomial Regression

```python
polynomial_model = Pipeline([
    ("polynomial", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler()),
    ("regression", LinearRegression())
])

polynomial_model.fit(X_train, y_train)

polynomial_prediction = polynomial_model.predict(X_test)
```

Polynomial Regression captures nonlinear relationships by transforming original features into polynomial features.

The pipeline performs three operations:

1. **PolynomialFeatures:** Generates squared and interaction features using degree 2.
2. **StandardScaler:** Standardizes the generated features.
3. **LinearRegression:** Trains the regression model using transformed features.

The `Pipeline` combines these operations into one sequence.

### Step 8: Evaluate Polynomial Regression

```python
polynomial_mse = mean_squared_error(y_test, polynomial_prediction)
polynomial_mae = mean_absolute_error(y_test, polynomial_prediction)
polynomial_r2 = r2_score(y_test, polynomial_prediction)
```

Calculates MSE, MAE and R² Score for Polynomial Regression, just as done for Linear Regression.

### Step 9: Display Results and Comparison Table

The program displays the performance metrics of both models and creates a Pandas DataFrame containing:

- Model name
- MSE
- MAE
- R² Score

It also saves the comparison table as:

`regression_results.csv`

### Step 10: Visualization

The program generates two figures.

**Figure 1 – Actual vs Predicted Values**

Uses scatter plots to compare actual house values with predicted house values for both regression models. The dashed diagonal line represents ideal predictions.

**Figure 2 – Model Performance Comparison**

Uses grouped bar graphs to compare MSE, MAE and R² Score of both models.

Both figures are saved as PNG files.

### Step 11: Final Conclusion

The program uses conditional statements (`if-else`) to compare the models.

It checks:
- Which model has lower MSE.
- Which model has lower MAE.
- Which model has higher R² Score.

Finally, it displays the conclusion and confirms successful execution.

## 4. Output and Results

| Evaluation Metric | Linear Regression | Polynomial Regression |
|---|---:|---:|
| MSE | 0.5559 | 0.4643 |
| MAE | 0.5332 | 0.4670 |
| R² Score | 0.5758 | 0.6457 |

**Conclusion:**

Polynomial Regression performs better than Linear Regression on this test dataset because it has lower MSE and MAE and a higher R² Score.

Therefore, Polynomial Regression provides better predictions for this particular experiment.

## 5. Dependencies Required

The program requires:

- Python 3
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## 6. Commands to Execute the Program

After installing the required dependencies, execute:

```bash
python3 regression.py
```

The program generates:

1. `regression_results.csv`
2. `figure1_actual_vs_predicted.png`
3. `figure2_model_comparison.png`


