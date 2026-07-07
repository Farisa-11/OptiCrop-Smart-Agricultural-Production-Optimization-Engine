# 🌱 OptiCrop: Smart Agricultural Production Optimization Engine

A Machine Learning-based web application that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions. The project is developed using **Python**, **Flask**, and **Scikit-learn** to support smart and sustainable farming.

---

## 📖 Overview

OptiCrop is an intelligent agricultural recommendation system that predicts the most suitable crop using machine learning techniques. By analyzing soil nutrients and environmental parameters, the system helps farmers make informed decisions to improve productivity and resource utilization.

The application accepts the following inputs:

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

- 🌾 Machine Learning-based crop recommendation
- 🌱 User-friendly web interface
- 📊 Data preprocessing and feature analysis
- ⚡ Fast and accurate predictions
- 💻 Flask backend integration
- 📱 Responsive web design
- 🌍 Supports sustainable farming practices

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- Bootstrap

### Backend

- Python
- Flask

### Machine Learning

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
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│      └── Crop_recommendation.csv
│
├── static/
│      ├── css/
│      │      └── style.css
│      │
│      └── images/
│             └── farm.jpg
│
└── templates/
       ├── index.html
       ├── about.html
       └── predict.html
```

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

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🤖 Machine Learning Workflow

```text
Agricultural Dataset
          │
          ▼
Data Preprocessing
          │
          ▼
Feature Selection
          │
          ▼
Train Machine Learning Model
          │
          ▼
Save Model (model.pkl)
          │
          ▼
Flask Web Application
          │
          ▼
User Inputs Agricultural Data
          │
          ▼
Crop Prediction
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### About Page

(Add screenshot here)

### Find Your Crop Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## 📈 Expected Output

Example Input

| Parameter | Value |
|-----------|------:|
| Nitrogen | 90 |
| Phosphorus | 42 |
| Potassium | 43 |
| Temperature | 20.8 |
| Humidity | 82 |
| pH | 6.5 |
| Rainfall | 202 |

Example Output

```text
Recommended Crop:
Rice
```

---

## 🌟 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation System
- Crop Disease Prediction
- IoT Sensor Integration
- Deep Learning Models
- Mobile Application
- Cloud Deployment

---

## 🎯 Conclusion

OptiCrop demonstrates how Machine Learning and Artificial Intelligence can be applied to modern agriculture for intelligent crop recommendation. The system improves farming efficiency by providing accurate crop predictions based on soil nutrients and environmental conditions, supporting sustainable and data-driven agricultural practices.

---

## 👩‍💻 Author

**Farisa Almas**

GitHub: https://github.com/Farisa-11

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
