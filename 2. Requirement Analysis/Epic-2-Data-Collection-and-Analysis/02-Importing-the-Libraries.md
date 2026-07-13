# Importing the Libraries

## Overview

The **OptiCrop: Smart Agricultural Production Optimization Engine** requires several Python libraries for data manipulation, visualization, machine learning, and model evaluation. These libraries provide the essential tools for preprocessing agricultural data, training machine learning models, generating crop recommendations, and evaluating prediction performance.

---

## Libraries Used

| Library | Purpose |
|----------|---------|
| **Pandas** | Used for loading, manipulating, and analyzing agricultural datasets. |
| **NumPy** | Provides numerical computing support and mathematical operations on arrays. |
| **Matplotlib** | Creates charts, graphs, and visualizations for data analysis. |
| **Seaborn** | Generates attractive statistical visualizations and analytical plots. |
| **Scikit-learn** | Provides machine learning algorithms, data preprocessing, model evaluation, and dataset splitting utilities. |
| **IPython** | Enhances interactive notebook functionality. |
| **ipywidgets** | Enables interactive widgets for data exploration and analysis. |

---

## Machine Learning Modules

The following Scikit-learn modules are imported for model development and evaluation:

- **KMeans** – Groups similar agricultural conditions using clustering.
- **train_test_split** – Splits the dataset into training and testing sets.
- **LogisticRegression** – Builds the crop recommendation classification model.
- **confusion_matrix** – Evaluates prediction accuracy by comparing actual and predicted values.
- **classification_report** – Generates performance metrics such as precision, recall, F1-score, and accuracy.

---

## Visualization Settings

The project configures Pandas display options to improve dataset readability and uses Matplotlib to generate clear and informative visualizations for agricultural data analysis.

---

## Python Code

```python
import pandas as pd
import numpy as np

pd.set_option('max_colwidth', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)

import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
plt.rcParams['figure.figsize'] = (12, 8)

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

from ipywidgets import interact

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

---

## Purpose

The imported libraries provide the foundation for:

- Loading and managing agricultural datasets.
- Performing data preprocessing and exploratory data analysis.
- Creating visualizations for agricultural insights.
- Training and evaluating machine learning models.
- Generating intelligent crop recommendations.
- Supporting interactive data exploration and analysis.

---

## Conclusion

Importing the required libraries establishes the development environment for the **OptiCrop: Smart Agricultural Production Optimization Engine**. These libraries enable efficient data processing, visualization, machine learning model development, and performance evaluation, forming the foundation of the crop recommendation system.
