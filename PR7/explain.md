---

# 8. Conceptual Explanation and Analysis

## 8.1 What is Clustering?

Clustering is an Unsupervised Machine Learning technique used to group similar data points together.

It does not require predefined output labels. Instead, it identifies patterns and similarities in the dataset and creates groups called clusters.

**In this practical:** We group mall customers based on their Annual Income and Spending Score to identify different types of customers.

For example:
- Customers with high income and high spending scores.
- Customers with high income and low spending scores.
- Customers with low income and high spending scores.
- Customers with low income and low spending scores.

This helps businesses understand customer behaviour and develop targeted marketing strategies.

## 8.2 K-Means Clustering

K-Means is a partition-based unsupervised learning algorithm that divides a dataset into K clusters.

**Working:**

1. Select the number of clusters (K).
2. Initialize K cluster centroids.
3. Calculate the distance of each data point from the centroids.
4. Assign each point to its nearest centroid.
5. Recalculate the centroids using the mean of the assigned points.
6. Repeat until the cluster assignments or centroids stop changing significantly.

**In this practical:** We use K-Means with K = 5 to divide the 200 mall customers into five groups based on annual income and spending score.

### Important terms

- **K:** Number of clusters.
- **Centroid:** Centre of a cluster, calculated using the mean of its data points.
- **Euclidean Distance:** Measures the straight-line distance between two data points.
- **Inertia:** Sum of squared distances of data points from their assigned cluster centroids.

## 8.3 Elbow Method

The Elbow Method is used to determine a suitable number of clusters for K-Means.

It calculates WCSS (Within-Cluster Sum of Squares) for different values of K.

**WCSS:** It measures the total squared distance between each data point and its assigned cluster centroid.

**Working:**

1. Run K-Means for different cluster counts, from K = 1 to K = 10.
2. Calculate WCSS for every value of K.
3. Plot the number of clusters against WCSS.
4. Identify the elbow point where the reduction in WCSS starts slowing down.
5. Select that value of K as a suitable cluster count.

**Why does WCSS decrease?**

As the number of clusters increases, data points generally become closer to their respective centroids, reducing WCSS.

However, increasing the number of clusters indefinitely is not useful. The Elbow Method helps find a balance between cluster compactness and the number of clusters.

**In this practical:** We inspect the Elbow Curve and select five clusters.

## 8.4 Hierarchical Clustering

Hierarchical Clustering is an unsupervised learning technique that creates a hierarchy of clusters.

Unlike K-Means, it does not initially require the number of clusters to be specified when constructing the hierarchy.

There are two main types:

1. **Agglomerative Clustering:** Bottom-up approach. Starts with individual data points and progressively merges similar clusters.
2. **Divisive Clustering:** Top-down approach. Starts with one large cluster and repeatedly divides it into smaller clusters.

**In this practical:** We implement Agglomerative Hierarchical Clustering.

### Working of Agglomerative Clustering

1. Initially, each customer is treated as an individual cluster.
2. Calculate distances between clusters.
3. Merge the two closest clusters.
4. Repeat the merging process.
5. Stop when the specified number of clusters is reached.

We use five clusters in our implementation.

## 8.5 Dendrogram

A Dendrogram is a tree-like diagram used to visualize the merging process in Hierarchical Clustering.

It helps determine a suitable number of clusters.

**How to interpret it:**

- The leaves represent individual data points.
- The branches represent cluster merging.
- The vertical axis represents the distance at which clusters are merged.
- Large vertical gaps indicate substantial differences between merging clusters.

A horizontal cut through the dendrogram can help identify the number of clusters.

**In this practical:** We generate the dendrogram using SciPy's `linkage()` and `dendrogram()` functions.

## 8.6 Ward Linkage

Ward linkage is a method used in Hierarchical Clustering to decide which clusters should be merged.

It selects the merge that produces the smallest increase in within-cluster variance.

It generally helps create compact and relatively homogeneous clusters.

**In this practical:** We use `method='ward'` in the dendrogram calculation and `linkage='ward'` in AgglomerativeClustering.

## 8.7 Distance Measurement

Both K-Means and Ward-based Hierarchical Clustering use Euclidean distance in this practical.

Euclidean distance measures the straight-line distance between two points.

For two points:

A = (x1, y1)

B = (x2, y2)

The formula is:

Distance = √[(x2 - x1)² + (y2 - y1)²]

A smaller distance indicates that two data points are closer to each other.

Since we use Annual Income and Spending Score, the distance is calculated using these two numerical features.

## 8.8 Cluster Visualization

We generate scatter plots to understand the clusters visually.

**K-Means visualization:**
- Each colour represents a different cluster.
- X markers represent the cluster centroids.
- Customers with similar income and spending patterns are grouped together.

**Hierarchical visualization:**
- Different colours represent the five generated hierarchical clusters.
- The plot helps observe how customers are distributed across groups.

These visualizations make it easier to understand the customer segments produced by both algorithms.

## 8.9 Evaluation Metrics and Analysis

Clustering is an Unsupervised Learning technique. Therefore, it does not normally use classification metrics such as Accuracy, Precision, Recall and F1-Score because predefined correct labels are not available in this dataset.

Instead, clustering quality can be evaluated using measures such as WCSS, Silhouette Score and Davies-Bouldin Index.

### Metrics used in this practical

**1. WCSS (Within-Cluster Sum of Squares)**

- Measures the sum of squared distances between data points and their assigned centroids.
- Lower WCSS indicates more compact clusters.
- Used in the Elbow Method to select a suitable number of clusters.

**2. Cluster Counts**

- Shows the number of customers assigned to each cluster.
- Helps understand the distribution and size of different customer groups.
- Calculated using `value_counts()`.

**3. Cluster-wise Mean Analysis**

- Calculates the average annual income and spending score for each cluster.
- Helps understand the characteristics of each customer group.
- Can be used to identify high-income, low-spending or high-spending customer segments.

### Additional clustering evaluation metrics

These metrics are useful for further evaluation but are not calculated in the current code.

**4. Silhouette Score**

- Measures how similar a data point is to its own cluster compared with other clusters.
- Its value ranges from -1 to +1.
- A score closer to +1 generally indicates better-separated clusters.
- A value near 0 indicates overlapping clusters.
- Negative values may indicate that some points are assigned to inappropriate clusters.

**5. Davies-Bouldin Index**

- Measures the similarity between clusters based on their compactness and separation.
- A lower value generally indicates better clustering.
- It is used to compare the quality of different clustering solutions.

**Important:** WCSS, cluster counts and cluster-wise mean analysis are directly relevant to the current implementation. Silhouette Score and Davies-Bouldin Index are additional metrics and would require extra code to calculate.

## 8.10 Comparison of K-Means and Hierarchical Clustering

| Parameter | K-Means | Hierarchical |
|---|---|---|
| Approach | Partition-based | Hierarchical |
| Method | Centroid-based | Cluster merging |
| Cluster formation | Divides data into K groups | Builds a hierarchy of groups |
| Number of clusters | Specified before fitting | Can be selected by cutting the dendrogram |
| Visualization | Scatter plot and centroids | Dendrogram and scatter plot |
| Scalability | Generally faster for large datasets | Can be computationally expensive |
| Practical implementation | K-Means algorithm | Agglomerative algorithm |

## 8.11 What Are We Actually Doing in This Practical?

In this practical, we are performing customer segmentation using Machine Learning.

We take the Mall Customers dataset containing 200 customer records and select two important features: Annual Income and Spending Score.

We then apply two clustering algorithms:

1. **K-Means:** Uses the Elbow Method to help select the number of clusters and groups customers into five clusters.
2. **Hierarchical Clustering:** Uses a Dendrogram to study the hierarchical relationships between customers and applies Agglomerative Clustering to generate five clusters.

Finally, we visualize the clusters, display the number of customers in each cluster, and analyze their income and spending behaviour.

The purpose is to understand customer purchasing patterns and identify different customer segments that can help businesses make better marketing decisions.
