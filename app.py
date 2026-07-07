from flask import Flask, render_template, request
import pickle
import pandas as pd

# Create Flask application
app = Flask(__name__)

# Load trained machine learning model
model = pickle.load(open("model.pkl", "rb"))

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

            # Create a DataFrame with feature names
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

            # Predict the crop
            prediction = model.predict(input_data)[0]

        except Exception as e:
            print("Error:", e)
            prediction = "Invalid input. Please enter valid values."

    return render_template("predict.html", prediction=prediction)

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)