# K-Means Clustering

## Overview

K-Means Clustering is an unsupervised machine learning algorithm used to group similar data points into clusters based on their feature similarity. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, K-Means clustering is applied to identify patterns among agricultural conditions such as soil nutrients and environmental parameters.

Before training the clustering model, the **Elbow Method** is used to determine the optimal number of clusters. The method evaluates different cluster values by calculating the **Within-Cluster Sum of Squares (WCSS)** and identifies the point where the decrease in WCSS begins to level off, known as the **elbow point**.

Based on the elbow graph, the optimal number of clusters is selected, and the K-Means model is trained using the agricultural dataset to group crops with similar characteristics.

---

## Objective

The objectives of this step are to:

- Determine the optimal number of clusters using the Elbow Method.
- Apply K-Means clustering to the agricultural dataset.
- Group crops with similar soil and environmental characteristics.
- Identify hidden agricultural patterns.
- Support intelligent crop recommendation and agricultural analysis.

---

## Python Code

### Step 1: Determine the Optimal Number of Clusters (Elbow Method)

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        max_iter=300,
        n_init=10,
        random_state=0
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()
```

---

### Step 2: Train the K-Means Model

```python
# Train the K-Means model
kmeans = KMeans(
    n_clusters=4,
    init='k-means++',
    max_iter=300,
    n_init=10,
    random_state=0
)

clusters = kmeans.fit_predict(X)

# Create a new dataframe with cluster labels
result = data.copy()
result['Cluster'] = clusters

# Display crops in each cluster
for i in range(4):
    print(f"\nCluster {i + 1}:")
    print(result[result['Cluster'] == i]['label'].unique())
```

---

## Elbow Method

The Elbow Method evaluates different values of **K** (number of clusters) by calculating the **Within-Cluster Sum of Squares (WCSS)**.

The optimal value of **K** is identified at the point where the reduction in WCSS begins to slow significantly, forming an "elbow" in the graph.

In this project, the elbow graph indicates that **4 clusters** provide an appropriate grouping of agricultural conditions.

---

## Sample Output

### Elbow Graph

The WCSS values decrease as the number of clusters increases. The graph shows a noticeable bend at **K = 4**, indicating the optimal number of clusters.

---

### Cluster Results

Example cluster groups may include crops such as:

**Cluster 1**

- Rice
- Pigeon Peas
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute

**Cluster 2**

- Maize
- Banana
- Grapes
- Watermelon
- Muskmelon
- Coconut
- Cotton

**Cluster 3**

- Chickpea
- Kidney Beans
- Moth Beans
- Mung Bean
- Black Gram
- Lentil
- Pomegranate
- Mango

**Cluster 4**

- Grapes
- Muskmelon

> *The exact crops within each cluster may vary depending on preprocessing steps and the selected random state.*

---

## Observations

The K-Means clustering process provides the following insights:

- The Elbow Method identifies the optimal number of clusters.
- Agricultural conditions are grouped based on feature similarity.
- Crops with similar environmental requirements are clustered together.
- The clustering process reveals hidden patterns within the agricultural dataset.
- The generated clusters support agricultural analysis and crop recommendation.

---

## Purpose

Applying K-Means clustering helps to:

- Discover hidden agricultural patterns.
- Group crops with similar growing conditions.
- Improve agricultural data analysis.
- Support intelligent decision-making.
- Enhance crop recommendation strategies.

---

## Expected Outcome

After completing this step:

- The optimal number of clusters is identified.
- The agricultural dataset is grouped into meaningful clusters.
- Similar crops are organized based on environmental conditions.
- The clustering results support further machine learning analysis and crop recommendation.

---

## Conclusion

K-Means Clustering plays an important role in the **OptiCrop: Smart Agricultural Production Optimization Engine** by grouping agricultural data into meaningful clusters based on soil nutrients and environmental conditions. The Elbow Method ensures that an appropriate number of clusters is selected, while the trained K-Means model uncovers valuable agricultural patterns that support intelligent crop recommendation and precision farming.
