# Splitting Data into Train and Test Sets

## Overview

Splitting the dataset into training and testing sets is an essential step in the machine learning workflow. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, the dataset is divided into **feature variables (X)** and the **target variable (y)** before training the machine learning model.

The feature variables include agricultural parameters such as **Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall**, while the target variable contains the **recommended crop label**.

The `train_test_split()` function from Scikit-learn is used to divide the dataset into training and testing subsets. The training set is used to build the model, while the testing set is used to evaluate its performance on unseen data.

---

## Objective

The objectives of this step are to:

- Separate the input features and target variable.
- Prepare the dataset for machine learning.
- Split the dataset into training and testing sets.
- Evaluate model performance using unseen data.
- Improve the reliability and accuracy of crop prediction.

---

## Python Code

```python
from sklearn.model_selection import train_test_split

# Separate features and target variable
X = data.drop('label', axis=1)
y = data['label']

# Display dataset dimensions
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

# Display the shapes of the training and testing sets
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)
```

---

## Sample Output

```text
Shape of X: (2200, 7)
Shape of y: (2200,)

Shape of X_train: (1760, 7)
Shape of X_test: (440, 7)
Shape of y_train: (1760,)
Shape of y_test: (440,)
```

> **Note:** If outlier removal or data preprocessing is performed before splitting, the dataset size may change (for example, from **2200** to **2062** records). In such cases, the shapes displayed will correspond to the processed dataset.

---

## Dataset Split

| Dataset | Purpose |
|----------|---------|
| **Training Set (80%)** | Used to train the machine learning model. |
| **Testing Set (20%)** | Used to evaluate the model on unseen data. |

---

## Observations

The dataset splitting process provides the following insights:

- The agricultural dataset is successfully divided into feature variables and target labels.
- The training dataset contains most of the records used for model learning.
- The testing dataset is reserved for unbiased model evaluation.
- Both datasets contain the same agricultural features.
- The split supports reliable machine learning model development and performance assessment.

---

## Purpose

Splitting the dataset helps to:

- Train the machine learning model effectively.
- Evaluate prediction performance on unseen data.
- Prevent overfitting.
- Measure model accuracy objectively.
- Improve the reliability of crop recommendations.

---

## Expected Outcome

After completing this step:

- The dataset is successfully divided into features and labels.
- Training and testing datasets are created.
- The machine learning model is ready for training.
- The testing dataset is available for model evaluation.

---

## Conclusion

Splitting the dataset into training and testing sets is an important step in developing the **OptiCrop: Smart Agricultural Production Optimization Engine**. This process enables the machine learning model to learn from historical agricultural data while ensuring reliable performance evaluation on unseen data, resulting in accurate and intelligent crop recommendations.
