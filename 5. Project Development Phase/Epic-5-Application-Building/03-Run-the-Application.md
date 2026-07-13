# OptiCrop: Smart Agricultural Production Optimization Engine

## Overview
OptiCrop is an advanced Machine Learning-powered smart agricultural recommendation system designed to support modern, data-driven farming practices. The application analyzes environmental and soil parameters to recommend the most suitable crop for cultivation, helping farmers maximize yield and improve resource utilization.

---

## Workspace
The project consists of the following main components:

- **Home Page** – Introduction to the OptiCrop system.
- **About Page** – Provides detailed information about the project's objectives and methodology.
- **FindYourCrop Page** – Allows users to enter environmental conditions and receive crop recommendations.

---

## Kanban

### Completed Tasks
- Designed Home Page UI
- Developed About Page
- Created Crop Prediction Form
- Integrated Machine Learning Model
- Connected Frontend with Backend
- Displayed Prediction Results
- Tested Application Functionality

### In Progress
- Model Accuracy Improvements
- UI Enhancements

### Future Enhancements
- Weather API Integration
- Fertilizer Recommendation Module
- Multi-language Support
- Mobile Application Development

---

## Run the Application

### Step 1: Open the Project
Open the project folder in **Visual Studio Code** and ensure all project files are imported correctly.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask pandas numpy scikit-learn
```

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Open the Application
After running the application, a local server URL will appear in the terminal:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

---

## Story

### Home Page
The Home page is displayed when the application launches. It introduces the OptiCrop system and provides navigation links to other pages.

### About Page
The About page explains the purpose and functionality of the project. The system uses environmental factors such as:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

These parameters are analyzed using Machine Learning algorithms to determine the most suitable crop for cultivation.

### FindYourCrop Page
The FindYourCrop page allows users to enter environmental and soil conditions. After clicking the **Predict** button, the model processes the inputs and returns a crop recommendation.

**Example Output:**

```text
Best crop for given conditions is coffee
```

---

## Workflow

```text
User Inputs Environmental Data
               ↓
Data Validation & Processing
               ↓
Machine Learning Prediction Model
               ↓
Crop Recommendation Generated
               ↓
Result Displayed to User
```

---

## Features

- User-friendly web interface
- Machine Learning-based crop recommendation
- Fast and accurate predictions
- Supports multiple environmental parameters
- Helps farmers make informed decisions
- Improves agricultural productivity

---

## Technologies Used

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

---

## Conclusion

OptiCrop provides an intelligent agricultural decision-support system that helps farmers identify the most suitable crop based on environmental and soil conditions. By leveraging Machine Learning techniques, the application promotes efficient resource utilization, improved crop yields, and sustainable farming practices.
