from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

# Base directory of the src folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "model.pkl")

# Create Flask application
app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

# Load trained machine learning model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# About Page
@app.route('/about')
def about():
    return render_template("about.html")

# Prediction Page
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    prediction = None

    if request.method == "POST":
        try:
            # Get input values from the form
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Create DataFrame for prediction
            input_data = pd.DataFrame(
                [[N, P, K, temperature, humidity, ph, rainfall]],
                columns=[
                    "N",
                    "P",
                    "K",
                    "temperature",
                    "humidity",
                    "ph",
                    "rainfall"
                ]
            )

            # Predict crop
            prediction = model.predict(input_data)[0]

        except Exception as e:
            print("Error:", e)
            prediction = "Invalid input. Please enter valid values."

    return render_template("predict.html", prediction=prediction)

# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)