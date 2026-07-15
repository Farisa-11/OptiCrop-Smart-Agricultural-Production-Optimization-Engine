# 🌱 OptiCrop: Smart Agricultural Production Optimization Engine

<p align="center">
  <img src="5.%20Project%20Development%20Phase/static/images/farm.jpg" alt="OptiCrop Banner" width="700">
</p>

A Machine Learning-based web application that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions. The project is developed using **Python**, **Flask**, and **Scikit-learn** to support smart, data-driven, and sustainable farming.

---

## 🚀 Project Status

✅ Completed and Successfully Tested

---

## 📑 Table of Contents

- Overview
- Features
- Technologies Used
- Project Structure
- Documentation
- Installation
- Running the Application
- Machine Learning Workflow
- Expected Output
- Future Enhancements
- Conclusion
- Author
- License

---

## 📖 Overview

OptiCrop is an intelligent agricultural recommendation system that predicts the most suitable crop using Machine Learning techniques. By analyzing soil nutrients and environmental conditions, the system recommends the best crop for cultivation, helping farmers improve productivity and promote sustainable farming.

The application accepts the following agricultural inputs:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

Based on these parameters, the trained machine learning model predicts the most suitable crop.

---

## ✨ Features

- 🌱 Machine Learning-based crop recommendation
- 🌾 Smart agricultural decision support
- 📊 Data preprocessing and visualization
- ⚡ Fast and accurate crop prediction
- 💻 Flask-based web application
- 📱 Responsive user interface
- 🌍 Sustainable farming support

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Backend

- Python
- Flask

### Machine Learning

- Random Forest Classifier
- Scikit-learn
- Pandas
- NumPy

### Tools

- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```text
OptiCrop-Smart-Agricultural-Production-Optimization-Engine
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── assets/
│   └── images/
│       └── farm.jpg
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── docs/
│   ├── 00-Pre-requisites.md
│   ├── 03-Entity-Relationship-Diagram.md
│   ├── 04-Workflow.md
│   ├── Conclusion/
│   │   └── 01-Conclusion.md
│   ├── Epic-1-Define-Problem-and-Understanding/
│   ├── Epic-2-Data-Collection-and-Analysis/
│   ├── Epic-3-Data-Pre-processing/
│   ├── Epic-4-Model-Building/
│   └── Epic-5-Application-Building/
│
├── models/
│   └── model.pkl
│
├── notebooks/
│   └── README.md
│
├── src/
│   ├── app.py
│   └── train_model.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── farm.jpg
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── predict.html
│
├── tests/
│   └── test_app.py
│
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📚 Documentation

The complete project documentation is available inside the **docs** folder.

| Document | Description |
|----------|-------------|
| 00-Pre-requisites.md | Software and environment setup |
| 03-Entity-Relationship-Diagram.md | Entity Relationship Diagram |
| 04-Workflow.md | Overall project workflow |
| Epic-1 | Problem Definition and Business Understanding |
| Epic-2 | Data Collection and Analysis |
| Epic-3 | Data Pre-processing |
| Epic-4 | Machine Learning Model Building |
| Epic-5 | Flask Application Development |
| Conclusion | Final Project Summary |

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Farisa-11/OptiCrop-Smart-Agricultural-Production-Optimization-Engine.git
```

### Open the Project

```bash
cd OptiCrop-Smart-Agricultural-Production-Optimization-Engine
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Flask application using:

```bash
python src/app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🤖 Machine Learning Workflow

```text
Agricultural Dataset
          │
          ▼
Data Collection
          │
          ▼
Data Pre-processing
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Feature Selection
          │
          ▼
Random Forest Model Training
          │
          ▼
Model Evaluation
          │
          ▼
Save Trained Model (model.pkl)
          │
          ▼
Flask Web Application
          │
          ▼
User Inputs Agricultural Parameters
          │
          ▼
Crop Prediction
          │
          ▼
Recommended Crop Displayed
```

---

## 📈 Expected Output

### Example Input

| Parameter | Value |
|-----------|------:|
| Nitrogen | 90 |
| Phosphorus | 42 |
| Potassium | 43 |
| Temperature | 20.8 |
| Humidity | 82 |
| Soil pH | 6.5 |
| Rainfall | 202 |

### Example Output

```text
Recommended Crop:
Rice
```

---

## 🌟 Future Enhancements

- 🌦️ Weather API Integration
- 🌱 Fertilizer Recommendation System
- 🦠 Crop Disease Detection
- 📡 IoT-enabled Smart Farming
- 🤖 Deep Learning Models
- ☁️ Cloud Deployment
- 📱 Android Application
- 📊 Agricultural Analytics Dashboard

---

## 🎯 Conclusion

OptiCrop demonstrates the practical application of Machine Learning in modern agriculture. By combining predictive analytics with soil and environmental data, the system provides accurate crop recommendations that improve productivity, optimize resource utilization, and support sustainable farming.

The project serves as a strong foundation for future developments in precision agriculture, smart farming, and intelligent agricultural decision-support systems.

---

## 👩‍💻 Author

**Farisa Almas**

GitHub: https://github.com/Farisa-11

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
