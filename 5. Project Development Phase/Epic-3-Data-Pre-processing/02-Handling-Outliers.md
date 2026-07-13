# Handling Outliers

## Overview

Outliers are observations that differ significantly from the majority of the data and may adversely affect the performance of machine learning models. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, outliers are identified using boxplots and detected mathematically using the **Interquartile Range (IQR)** method.

The IQR technique is applied to identify extreme values in the selected agricultural feature and remove them from the dataset. This improves data quality, reduces noise, and enhances the accuracy of crop recommendation models.

---

## Objective

The objectives of this step are to:

- Identify outliers in the agricultural dataset.
- Visualize feature distributions using boxplots.
- Calculate the Interquartile Range (IQR).
- Remove extreme values from the selected feature.
- Prepare a clean dataset for machine learning.

---

## Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize outliers using boxplots
plt.figure(figsize=(8, 4))
sns.boxplot(data=data)

plt.title("Boxplot of Agricultural Features")
plt.show()

# Calculate IQR for the Phosphorus feature
Q1 = data['P'].quantile(0.25)
Q3 = data['P'].quantile(0.75)

IQR = Q3 - Q1

# Remove outliers using the IQR method
filter = (
    (data['P'] >= Q1 - 1.5 * IQR) &
    (data['P'] <= Q3 + 1.5 * IQR)
)

data = data.loc[filter]
```

---

## IQR Formula

The Interquartile Range (IQR) is calculated as:

**IQR = Q3 − Q1**

Where:

- **Q1** = First Quartile (25th percentile)
- **Q3** = Third Quartile (75th percentile)

The outlier boundaries are calculated as:

- **Lower Bound = Q1 − 1.5 × IQR**
- **Upper Bound = Q3 + 1.5 × IQR**

Any observation lying outside these boundaries is considered an outlier.

---

## Sample Output

The boxplot displays the distribution of the following agricultural features:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The visualization highlights observations that fall outside the normal range, indicating the presence of outliers. The IQR method is then used to remove outliers from the **Phosphorus (P)** feature.

---

## Observations

The outlier analysis reveals the following:

- Boxplots effectively identify extreme values in the agricultural dataset.
- The **Phosphorus (P)** feature contains observations outside the acceptable IQR range.
- The IQR method successfully detects and removes these extreme values.
- Removing outliers improves data consistency and reduces the influence of abnormal observations.
- The cleaned dataset is more suitable for machine learning model training.

---

## Purpose

Handling outliers helps to:

- Improve dataset quality.
- Reduce the impact of extreme values.
- Increase model accuracy and reliability.
- Improve prediction performance.
- Prepare the dataset for preprocessing and machine learning.

---

## Expected Outcome

After completing this step:

- Outliers are identified using boxplots.
- Extreme values are detected using the IQR method.
- Outliers are removed from the selected feature.
- The dataset becomes cleaner and more reliable for machine learning.

---

## Conclusion

Handling outliers is an important data preprocessing step in the **OptiCrop: Smart Agricultural Production Optimization Engine**. By identifying outliers through boxplots and removing extreme values using the Interquartile Range (IQR) method, the dataset becomes more consistent and reliable. This improves the performance of machine learning models and contributes to more accurate and dependable crop recommendations.
