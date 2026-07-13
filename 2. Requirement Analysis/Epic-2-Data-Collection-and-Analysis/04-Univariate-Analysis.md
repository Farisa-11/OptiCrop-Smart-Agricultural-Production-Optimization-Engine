# Univariate Analysis

## Overview

Univariate analysis is the process of analyzing each feature in the dataset individually to understand its distribution, central tendency, spread, and overall characteristics. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, univariate analysis helps identify the distribution of important agricultural parameters such as soil nutrients and environmental conditions before building machine learning models.

Visualization techniques such as histograms with Kernel Density Estimation (KDE) are used to analyze the distribution of each feature and identify possible patterns, skewness, or outliers.

---

## Objective

The objectives of this step are to:

- Analyze each agricultural feature independently.
- Understand the distribution of soil and environmental parameters.
- Identify potential outliers or skewed distributions.
- Gain insights into the dataset before preprocessing.
- Support feature selection and machine learning model development.

---

## Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

# List of numerical features
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Create subplots
plt.figure(figsize=(18, 10))

for i, feature in enumerate(features):
    plt.subplot(2, 4, i + 1)
    sns.histplot(data[feature], kde=True)
    plt.title(f'Distribution of {feature}')

plt.tight_layout()
plt.show()
```

---

## Sample Output

The generated plots display the distribution of the following agricultural parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Each graph illustrates how the values of an individual feature are distributed throughout the dataset.

---

## Observations

The univariate analysis reveals the following insights:

- **Nitrogen (N):** Shows variation across different agricultural conditions with multiple concentration ranges.
- **Phosphorus (P):** Displays a moderately distributed pattern with noticeable peaks.
- **Potassium (K):** Exhibits a wide distribution, indicating different soil nutrient levels.
- **Temperature:** Mostly follows a near-normal distribution with values concentrated around the average temperature.
- **Humidity:** Most observations fall within higher humidity ranges, indicating humid agricultural conditions.
- **Soil pH:** Values are concentrated around neutral pH levels, making the dataset suitable for a variety of crops.
- **Rainfall:** Displays a wider spread, reflecting different climatic conditions across agricultural regions.

---

## Purpose

Performing univariate analysis helps to:

- Understand the distribution of each feature.
- Detect unusual values and possible outliers.
- Identify skewness in agricultural parameters.
- Validate data quality before preprocessing.
- Support better feature engineering and model training.

---

## Expected Outcome

After completing this step:

- Individual feature distributions are visualized.
- Important characteristics of each agricultural parameter are understood.
- Potential data quality issues can be identified.
- The dataset becomes ready for further exploratory analysis and preprocessing.

---

## Conclusion

Univariate analysis provides valuable insights into the distribution of soil nutrients and environmental parameters in the **Crop Recommendation** dataset. Understanding these individual feature distributions helps improve data preprocessing, feature engineering, and machine learning model development, contributing to more accurate and reliable crop recommendations in the **OptiCrop: Smart Agricultural Production Optimization Engine**.
