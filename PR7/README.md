# Practical 7: Clustering Techniques

## 1. Aim

To implement K-Means Clustering and Hierarchical Clustering on a real-world dataset. Use the Elbow Method and Dendrogram to determine the optimal number of clusters and analyze the generated clusters.

## 2. Libraries Used

- **Pandas:** Used to load and manipulate the dataset.
- **Matplotlib:** Used to visualize the Elbow Curve, Dendrogram, and clusters.
- **Scikit-learn:** Provides K-Means and Agglomerative Hierarchical Clustering algorithms.
- **SciPy:** Used to generate the hierarchical linkage and Dendrogram.

## 3. Dataset Used

**Mall Customers Dataset**

This dataset contains 200 customer records with the following attributes:

- CustomerID: Unique customer ID.
- Gender: Customer's gender.
- Age: Customer's age.
- Annual Income (k$): Annual income in thousands of dollars.
- Spending Score (1-100): Customer's spending score.

For clustering, only two features are selected:

- Annual Income (k$)
- Spending Score (1-100)

These features help group customers according to their income and spending behaviour.

### Dataset Access

The dataset is loaded using Pandas:

```python
data = pd.read_csv("Mall_Customers.csv")
```

The CSV file must be present in the working directory, preferably in the same folder as the Python code.

## 4. Code Explanation

### Step 1: Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
```

Imports the required libraries for dataset handling, visualization, K-Means, Hierarchical Clustering, and Dendrogram generation.

### Step 2: Load Dataset

```python
data = pd.read_csv("Mall_Customers.csv")

print(data.head())
```

Loads the customer dataset from a CSV file. The `head()` function displays the first five records to understand the dataset.

### Step 3: Select Features

```python
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
```

Selects annual income and spending score for clustering.

These numerical features are used to calculate distances between customers.

### Step 4: Elbow Method

```python
wcss = []

for k in range(1, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)
```

The Elbow Method helps determine the optimal number of clusters.

- WCSS stands for Within-Cluster Sum of Squares.
- It measures the sum of squared distances between data points and their cluster centroids.
- The loop tests different cluster counts from 1 to 10.
- `inertia_` stores the WCSS value for each model.

The WCSS values are plotted against the number of clusters. The point where the decrease in WCSS starts slowing down is called the elbow point.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')

plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")

plt.show()
```

This displays the Elbow Curve. In this practical, K = 5 is selected based on the observed elbow.

### Step 5: Apply K-Means Clustering

```python
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

data['KMeans_Cluster'] = kmeans.fit_predict(X)
```

K-Means divides customers into five clusters based on their similarity.

- `n_clusters=5`: Creates five clusters.
- `random_state=42`: Ensures reproducible results.
- `n_init=10`: Runs the algorithm with ten different centroid initializations.
- `fit_predict()`: Trains the model and assigns a cluster label to every customer.

The cluster labels are stored in a new column called `KMeans_Cluster`.

### Step 6: Display K-Means Results

```python
print(data[
    ['CustomerID',
     'Annual Income (k$)',
     'Spending Score (1-100)',
     'KMeans_Cluster']
].head(20))
```

Displays the first 20 customers along with their assigned cluster numbers.

### Step 7: Visualize K-Means Clusters

```python
plt.figure(figsize=(8, 6))

plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=data['KMeans_Cluster'],
    s=50
)

centers = kmeans.cluster_centers_

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("K-Means Clustering")

plt.legend()
plt.show()
```

Creates a scatter plot of the five K-Means clusters.

- Different colours represent different clusters.
- Centroids represent the centres of the clusters.
- The X marker highlights the centroids.

### Step 8: Generate Hierarchical Clustering Dendrogram

```python
linked = linkage(X, method='ward')

plt.figure(figsize=(12, 6))

dendrogram(linked)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")

plt.show()
```

A Dendrogram is a tree-like diagram that shows how individual data points or clusters are progressively merged.

- `linkage()`: Calculates the hierarchical merging of clusters.
- `method='ward'`: Minimizes the increase in within-cluster variance when merging clusters.
- `dendrogram()`: Displays the hierarchical relationships.

The Dendrogram helps determine the suitable number of clusters by observing the vertical distances between merging clusters.

### Step 9: Apply Agglomerative Hierarchical Clustering

```python
hierarchical = AgglomerativeClustering(
    n_clusters=5,
    linkage='ward'
)

data['Hierarchical_Cluster'] = hierarchical.fit_predict(X)
```

Applies Agglomerative Hierarchical Clustering using five clusters.

It follows a bottom-up approach:

1. Initially, every customer is treated as a separate cluster.
2. The closest clusters are progressively merged.
3. Merging continues until five clusters remain.

The assigned cluster labels are stored in `Hierarchical_Cluster`.

### Step 10: Display Hierarchical Clustering Results

```python
print(data[
    ['CustomerID',
     'Annual Income (k$)',
     'Spending Score (1-100)',
     'Hierarchical_Cluster']
].head(20))
```

Displays the first 20 customers and their hierarchical cluster assignments.

### Step 11: Visualize Hierarchical Clusters

```python
plt.figure(figsize=(8, 6))

plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=data['Hierarchical_Cluster'],
    s=50
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Hierarchical Clustering")

plt.show()
```

Creates a scatter plot showing customers grouped into five hierarchical clusters using different colours.

### Step 12: Display Cluster Counts

```python
print(data['KMeans_Cluster'].value_counts())

print(data['Hierarchical_Cluster'].value_counts())
```

Displays the number of customers assigned to each cluster by both algorithms.

This helps compare the distribution of customers across the generated clusters.

## 5. Important Concepts

| Concept | Explanation |
|---|---|
| Clustering | Unsupervised learning technique that groups similar data points. |
| K-Means | Divides data into K clusters using cluster centroids. |
| Centroid | Centre point of a cluster. |
| WCSS | Sum of squared distances between data points and their centroids. |
| Elbow Method | Helps determine the suitable number of K-Means clusters. |
| Hierarchical Clustering | Creates a hierarchy of clusters by progressively merging or splitting groups. |
| Agglomerative Clustering | Bottom-up hierarchical clustering technique. |
| Dendrogram | Tree diagram representing the merging of clusters. |
| Ward Linkage | Merges clusters while minimizing the increase in within-cluster variance. |

## 6. Result

K-Means Clustering and Agglomerative Hierarchical Clustering were successfully implemented on the Mall Customers dataset.

The Elbow Method and Dendrogram were generated to help determine the optimal number of clusters. Five clusters were selected for both algorithms.

The generated scatter plots and cluster counts were used to visualize and analyze the customer groups.

## 7. Dependencies and Execution

Required Python libraries:

- pandas
- matplotlib
- scikit-learn
- scipy

The dataset file `Mall_Customers.csv` must be kept in the working directory.

The program can run without an internet connection once Python, the required libraries, and the dataset file are available.
