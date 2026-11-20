 

## 7. Conceptual Explanation

### 1. What is Regression?

Regression is a supervised machine learning technique used to predict a continuous numerical value based on input features.

In this practical, we use regression to predict the **median house value** based on features such as median income, house age, number of rooms, population, and location.

We implement two regression techniques:
- Linear Regression
- Polynomial Regression

### 2. Linear Regression

Linear Regression is a machine learning algorithm that establishes a linear relationship between input features and the target variable.

It tries to find the best-fitting straight line that minimizes the difference between actual and predicted values.

**Basic equation:**

`y = b0 + b1x`

Where:
- `y` = Predicted value
- `x` = Input feature
- `b0` = Intercept
- `b1` = Coefficient or slope

In this practical, Linear Regression uses the housing dataset features to predict house values by learning their linear relationships.

### 3. Polynomial Regression

Polynomial Regression is used when the relationship between input features and the target variable is not purely linear.

It transforms the original features into polynomial features, such as squares and interaction terms, and then applies Linear Regression.

For example, a degree 2 polynomial can include:

`x, x²`

In our practical, we use `PolynomialFeatures(degree=2)` to generate additional features.

**Why do we use Polynomial Regression?**

It helps the model learn more complex relationships between features and house prices compared to a simple linear model.

### 4. Feature Scaling – StandardScaler

Feature scaling is the process of bringing numerical features to a similar scale.

In our practical, `StandardScaler` is used in the Polynomial Regression pipeline.

It transforms features so that they have approximately:
- Mean = 0
- Standard Deviation = 1

This is useful because polynomial features can have different numerical ranges. Scaling helps the model work more effectively.

### 5. Train-Test Split

We divide the dataset into two parts:

- **Training Data (80%):** Used to train the machine learning model.
- **Testing Data (20%):** Used to evaluate the model on unseen data.

We use `train_test_split()` for this purpose.

`random_state=42` ensures that the same random split is produced whenever we run the code, making the results reproducible.

### 6. Model Evaluation Metrics

After training both models, we evaluate their performance using three metrics.

**A. Mean Squared Error (MSE)**

MSE calculates the average of the squared differences between actual and predicted values.

- It gives higher penalties to larger prediction errors.
- Lower MSE indicates better performance.
- An MSE of 0 means perfect predictions.

**B. Mean Absolute Error (MAE)**

MAE calculates the average absolute difference between actual and predicted values.

- It measures how far predictions are from actual values on average.
- It is easy to understand because it uses the same unit as the target variable.
- Lower MAE indicates better performance.

**C. R² Score (R-Squared Score)**

R² Score measures how well the model explains the variation in the target variable.

- R² = 1 means perfect prediction.
- R² = 0 means the model performs like predicting the mean value.
- A higher R² score generally indicates a better model.

**Comparison of Evaluation Metrics**

| Metric | Measures | Better Result |
|---|---|---|
| MSE | Average squared prediction error | Lower |
| MAE | Average absolute prediction error | Lower |
| R² Score | How well the model explains target variation | Higher |

### 7. Pipeline in Polynomial Regression

A Pipeline combines multiple machine learning steps into a single process.

In our practical, the Polynomial Regression pipeline contains three steps:

1. `PolynomialFeatures`: Generates polynomial and interaction features of degree 2.
2. `StandardScaler`: Scales the generated features.
3. `LinearRegression`: Trains the regression model using the transformed features.

The pipeline ensures that these operations are performed in the correct sequence. It also helps prevent data leakage because the transformations are fitted using training data.

### 8. Model Comparison

After evaluating both models, we compare their MSE, MAE, and R² scores.

Our obtained results are:

| Metric | Linear Regression | Polynomial Regression |
|---|---:|---:|
| MSE | 0.5559 | 0.4643 |
| MAE | 0.5332 | 0.4670 |
| R² Score | 0.5758 | 0.6457 |

From the results:
- Polynomial Regression has lower MSE.
- Polynomial Regression has lower MAE.
- Polynomial Regression has a higher R² score.

Therefore, **Polynomial Regression performs better than Linear Regression on our test dataset.**

### 9. Visualizations

We generate two graphs to understand and compare model performance.

**A. Actual vs Predicted Values**

This scatter plot compares the actual house values with the values predicted by the model.

- X-axis represents actual values.
- Y-axis represents predicted values.
- The diagonal reference line represents ideal predictions.
- Points closer to the diagonal line indicate more accurate predictions.

**B. Model Comparison Graph**

This grouped bar graph compares Linear Regression and Polynomial Regression using MSE, MAE, and R² Score.

It provides a visual comparison of the performance of both models. Since these metrics have different numerical scales, the exact values in the comparison table should be used for accurate interpretation.

### 10. Overall Working of the Practical

The practical follows these steps:

1. Load the California Housing dataset.
2. Separate input features and target variable.
3. Divide the dataset into training and testing sets.
4. Train the Linear Regression model.
5. Generate polynomial features and scale them.
6. Train the Polynomial Regression model.
7. Predict house values using both models.
8. Calculate MSE, MAE, and R² Score.
9. Compare the performance of both models.
10. Generate graphs and display the final conclusion.

**Final Conclusion:** Both Linear Regression and Polynomial Regression are implemented and evaluated. Based on the obtained results, Polynomial Regression performs better on this dataset because it achieves lower prediction errors and a higher R² score.
