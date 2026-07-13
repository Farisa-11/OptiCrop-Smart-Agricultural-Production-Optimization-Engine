# Bivariate Analysis

## Overview

Bivariate analysis examines the relationship between two variables to identify patterns, associations, and trends within the dataset. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, bivariate analysis is performed to understand how agricultural and environmental parameters influence crop recommendations.

In this step, the relationship between **humidity** and **crop labels** is visualized using a scatter plot. This helps identify how different crops are associated with varying humidity levels, providing valuable insights for crop prediction and agricultural decision-making.

---

## Objective

The objectives of this step are to:

- Analyze the relationship between humidity and crop labels.
- Identify patterns between environmental conditions and crop suitability.
- Understand how humidity influences crop recommendations.
- Support feature analysis before machine learning model development.
- Gain insights for intelligent agricultural decision-making.

---

## Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot between humidity and crop label
plt.figure(figsize=(10, 8))

sns.scatterplot(data=data, x='humidity', y='label')

plt.title("Relationship between Humidity and Crop Labels")
plt.xlabel("Humidity (%)")
plt.ylabel("Crop Label")

plt.show()
```

---

## Sample Output

The scatter plot displays the relationship between **humidity** and different **crop labels**. Each point represents an observation in the dataset, showing the humidity level associated with a particular crop.

---

## Observations

The bivariate analysis reveals the following insights:

- Different crops are associated with different humidity ranges.
- Crops such as **rice**, **banana**, **papaya**, and **coconut** are generally associated with higher humidity levels.
- Crops such as **chickpea** and **kidneybeans** are associated with relatively lower humidity levels.
- Some crops exhibit overlapping humidity ranges, indicating that additional features such as soil nutrients, rainfall, and temperature are required for accurate crop prediction.
- Humidity is an important environmental parameter that contributes significantly to crop recommendation.

---

## Purpose

Performing bivariate analysis helps to:

- Understand relationships between two variables.
- Identify environmental factors influencing crop selection.
- Detect patterns useful for predictive modeling.
- Support feature selection and model development.
- Improve the accuracy of crop recommendation systems.

---

## Expected Outcome

After completing this step:

- The relationship between humidity and crop labels is visualized.
- Crop-specific humidity patterns are identified.
- Environmental trends supporting crop recommendation are understood.
- The dataset becomes better prepared for multivariate analysis and machine learning.

---

## Conclusion

Bivariate analysis provides valuable insights into the relationship between humidity and crop recommendations in the **Crop Recommendation** dataset. Understanding these relationships helps identify important environmental factors affecting crop growth and supports the development of more accurate machine learning models in the **OptiCrop: Smart Agricultural Production Optimization Engine**.
