# Read the Dataset

## Overview

The **OptiCrop: Smart Agricultural Production Optimization Engine** uses the **Crop_recommendation.csv** dataset as the primary source for agricultural analysis and crop recommendation. The dataset is loaded into the application using the Pandas `read_csv()` function, which reads the CSV file into a DataFrame for efficient data manipulation, exploration, and machine learning.

After loading the dataset, the first five records are displayed using the `head()` function to verify that the dataset has been imported successfully and to examine its structure, feature columns, and target variable.

---

## Objective

The objectives of this step are to:

- Load the agricultural dataset into the Python environment.
- Verify that the dataset has been imported successfully.
- Examine the dataset structure and feature columns.
- Understand the input features and target variable.
- Prepare the dataset for preprocessing, visualization, and machine learning.

---

## Python Code

```python
# Import the dataset
data = pd.read_csv("dataset/Crop_recommendation.csv")

# Display the first five rows
data.head()
```

---

## Sample Output

The first five records of the dataset are displayed below.

| N | P | K | Temperature (°C) | Humidity (%) | pH | Rainfall (mm) | Label |
|---:|---:|---:|----------------:|-------------:|----:|--------------:|-------|
| 90 | 42 | 43 | 20.88 | 82.00 | 6.50 | 202.94 | Rice |
| 85 | 58 | 41 | 21.77 | 80.32 | 7.04 | 226.66 | Rice |
| 60 | 55 | 44 | 23.00 | 82.32 | 7.84 | 263.96 | Rice |
| 74 | 35 | 40 | 26.49 | 80.16 | 6.98 | 242.86 | Rice |
| 78 | 42 | 42 | 20.13 | 81.60 | 7.63 | 262.72 | Rice |

---

## Dataset Features

| Feature | Description |
|----------|-------------|
| **N** | Nitrogen content in the soil |
| **P** | Phosphorus content in the soil |
| **K** | Potassium content in the soil |
| **Temperature** | Temperature in degrees Celsius (°C) |
| **Humidity** | Relative humidity (%) |
| **pH** | Soil pH value |
| **Rainfall** | Annual rainfall (mm) |
| **Label** | Recommended crop |

---

## Purpose

Reading the dataset enables the system to:

- Load agricultural data into memory.
- Verify the integrity and structure of the dataset.
- Perform exploratory data analysis (EDA).
- Prepare the dataset for preprocessing.
- Train and evaluate machine learning models.
- Generate accurate crop recommendations.

---

## Expected Outcome

After executing the code:

- The dataset is successfully loaded into a Pandas DataFrame.
- The first five records are displayed.
- The dataset structure is verified.
- The data is ready for preprocessing, visualization, model training, and crop prediction.

---

## Conclusion

Loading the **Crop_recommendation.csv** dataset is the first step in the machine learning workflow of the **OptiCrop: Smart Agricultural Production Optimization Engine**. Successfully importing and validating the dataset ensures that the agricultural data is prepared for preprocessing, exploratory data analysis, machine learning model development, and intelligent crop recommendation.
