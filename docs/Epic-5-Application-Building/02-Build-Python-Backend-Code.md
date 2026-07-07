# Build Python Backend Code

## Overview

The Python backend serves as the core component of the **OptiCrop: Smart Agricultural Production Optimization Engine**, connecting the web interface with the trained machine learning model. The backend is developed using the **Flask** web framework and is responsible for loading the trained crop prediction model, managing application routes, processing user inputs, generating crop recommendations, and displaying prediction results.

The trained model is loaded from the saved **model.pkl** file using the **Pickle** library. Agricultural parameters entered by the user through the web interface are converted into numerical values and passed to the machine learning model, which predicts the most suitable crop based on the provided conditions.

---

## Objective

The objectives of this step are to:

- Initialize the Flask web application.
- Load the trained machine learning model.
- Define routes for application pages.
- Receive user input from HTML forms.
- Predict suitable crops using the trained model.
- Display prediction results to users through the web interface.

---

## Python Code

### Step 1: Import Required Libraries

```python
import numpy as np
import pickle
from flask import Flask, request, render_template
```

---

### Step 2: Initialize Flask Application and Load Model

```python
app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open("model.pkl", "rb"))
```

---

### Step 3: Define Application Routes

```python
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/findyourcrop')
def findyourcrop():
    return render_template("findyourcrop.html")
```

---

### Step 4: Predict Crop Recommendation

```python
@app.route('/predict', methods=['POST'])
def predict():

    features = [float(x) for x in request.form.values()]
    features = [np.array(features)]

    prediction = model.predict(features)
    output = prediction[0]

    return render_template(
        "findyourcrop.html",
        prediction_text="Best crop for given conditions is {}".format(output)
    )
```

---

### Step 5: Run the Flask Application

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

## Backend Workflow

The backend performs the following operations:

1. Initialize the Flask application.
2. Load the trained machine learning model (`model.pkl`).
3. Render the Home, About, and FindYourCrop pages.
4. Receive agricultural parameters submitted through the prediction form.
5. Convert the user inputs into numerical values.
6. Pass the processed data to the trained machine learning model.
7. Predict the most suitable crop.
8. Display the predicted crop recommendation on the web page.

---

## Route Description

| Route | Purpose |
|--------|---------|
| **/** | Displays the Home page. |
| **/about** | Displays project information and objectives. |
| **/findyourcrop** | Displays the crop prediction form. |
| **/predict** | Processes user input and generates crop recommendations. |

---

## Observations

The backend implementation provides the following functionality:

- Successfully initializes the Flask application.
- Loads the trained machine learning model into memory.
- Supports navigation between application pages.
- Accepts agricultural parameters from users.
- Predicts the most suitable crop using the trained model.
- Displays prediction results dynamically on the web interface.

---

## Purpose

Building the Python backend helps to:

- Connect the web interface with the machine learning model.
- Process user inputs efficiently.
- Generate real-time crop recommendations.
- Enable intelligent agricultural decision-making.
- Support deployment of the crop recommendation system.

---

## Expected Outcome

After completing this step:

- The Flask application starts successfully.
- The trained model is loaded correctly.
- Users can navigate between application pages.
- Agricultural parameters are processed successfully.
- Crop predictions are generated instantly.
- Prediction results are displayed on the web interface.

---

## Conclusion

The Python backend is an essential component of the **OptiCrop: Smart Agricultural Production Optimization Engine**. By integrating Flask with the trained machine learning model, it manages application routing, processes user-provided agricultural parameters, and generates accurate crop recommendations. This integration enables users to interact with the system through a user-friendly web interface and receive intelligent, data-driven crop predictions that support precision agriculture and sustainable farming practices.
