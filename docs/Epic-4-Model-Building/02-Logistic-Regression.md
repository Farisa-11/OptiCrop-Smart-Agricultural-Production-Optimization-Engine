# Logistic Regression

## Overview

Logistic Regression is a supervised machine learning algorithm used for classification tasks. In the **OptiCrop: Smart Agricultural Production Optimization Engine**, Logistic Regression is used to predict the most suitable crop based on agricultural and environmental parameters such as soil nutrients, temperature, humidity, pH, and rainfall.

The model is trained using the training dataset and then used to predict crop labels for unseen testing data. Its performance is evaluated to measure the accuracy and effectiveness of the crop recommendation system.

---

## Objective

The objectives of this step are to:

- Train a Logistic Regression classification model.
- Learn the relationship between agricultural features and crop labels.
- Predict suitable crops for new agricultural conditions.
- Evaluate model performance using unseen test data.
- Support intelligent crop recommendation.

---

## Python Code

```python
from sklearn.linear_model import LogisticRegression

# Create the Logistic Regression model
model = LogisticRegression(
    max_iter=1000,
    random_state=0
)

# Train the model
model.fit(X_train, y_train)

# Predict crop labels
y_pred = model.predict(X_test)

# Display the trained model
print(model)
```

---

## Sample Output

```text
LogisticRegression(max_iter=1000, random_state=0)
```

> **Note:** If the model displays a convergence warning (for example, *"lbfgs failed to converge"*), increasing the `max_iter` value or scaling the input features before training can help the optimization algorithm converge successfully.

---

## Model Workflow

The Logistic Regression model performs the following steps:

1. Train the model using the training dataset.
2. Learn relationships between agricultural features and crop labels.
3. Predict crop labels for unseen testing data.
4. Compare predicted labels with actual labels.
5. Evaluate model performance using accuracy and classification metrics.

---

## Observations

The Logistic Regression model provides the following insights:

- The model successfully learns relationships between agricultural features and crop labels.
- Crop predictions are generated for unseen testing samples.
- Soil nutrients and environmental parameters significantly influence crop prediction.
- The trained model can be integrated into the crop recommendation system.
- Performance can be evaluated using metrics such as Accuracy, Confusion Matrix, Precision, Recall, and F1-Score.

---

## Purpose

Implementing Logistic Regression helps to:

- Build an effective crop classification model.
- Predict suitable crops based on agricultural conditions.
- Support precision agriculture.
- Improve farming decision-making.
- Evaluate machine learning performance.

---

## Expected Outcome

After completing this step:

- The Logistic Regression model is successfully trained.
- Crop predictions are generated for the testing dataset.
- The trained model is ready for performance evaluation.
- The prediction results support intelligent crop recommendation.

---

## Conclusion

Logistic Regression serves as an effective supervised machine learning algorithm in the **OptiCrop: Smart Agricultural Production Optimization Engine**. By learning patterns from soil nutrients and environmental conditions, the model predicts suitable crops for cultivation, enabling accurate crop recommendations and supporting data-driven agricultural decision-making.
