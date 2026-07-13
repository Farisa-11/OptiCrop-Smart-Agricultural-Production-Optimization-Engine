# Building HTML Pages

## Overview

The **OptiCrop: Smart Agricultural Production Optimization Engine** provides a user-friendly web interface developed using **HTML** and integrated with the **Flask** framework. The application consists of multiple web pages that enable users to navigate through the system, learn about the project, and obtain crop recommendations based on agricultural and environmental parameters.

The HTML pages include a **Home** page, an **About** page, and a **FindYourCrop** page. Together, these pages provide seamless navigation, project information, and an interactive crop prediction interface.

---

## Objective

The objectives of this step are to:

- Design a responsive and user-friendly web interface.
- Provide smooth navigation between application pages.
- Display project information and objectives.
- Collect agricultural input parameters from users.
- Integrate the frontend with the Flask backend for crop prediction.

---

# Home Page

## Description

The **Home** page serves as the entry point of the OptiCrop application. It contains a navigation bar with links to different sections of the application and introduces the purpose of the crop recommendation system.

The page provides quick access to:

- Home
- About
- FindYourCrop

It also displays a brief introduction to the Smart Agricultural Production Optimization Engine.

### Features

- Navigation bar
- Project title
- Project introduction
- Easy access to application modules

---

# About Page

## Description

The **About** page provides detailed information about the OptiCrop project. It explains the objectives of intelligent crop prediction and describes how machine learning techniques utilize soil nutrients and environmental parameters to generate crop recommendations.

The page highlights the benefits of the system, including:

- Data-driven agricultural decision-making
- Improved crop productivity
- Efficient resource utilization
- Sustainable farming practices

### Features

- Project overview
- System objectives
- Machine learning explanation
- Benefits of crop recommendation

---

# FindYourCrop Page

## Description

The **FindYourCrop** page contains the crop prediction form that allows users to enter agricultural and environmental parameters required by the machine learning model.

The collected input values are submitted to the Flask backend using an HTML form, where the trained Logistic Regression model predicts the most suitable crop.

### Input Parameters

| Parameter | Description |
|------------|-------------|
| Nitrogen (N) | Nitrogen content in the soil |
| Phosphorus (P) | Phosphorus content in the soil |
| Potassium (K) | Potassium content in the soil |
| Temperature | Temperature (°C) |
| Humidity | Relative humidity (%) |
| pH | Soil pH value |
| Rainfall | Annual rainfall (mm) |

### Features

- User-friendly input form
- Data validation using required fields
- Form submission to Flask backend
- Display of crop prediction results

---

## HTML Components Used

The web application utilizes the following HTML components:

| Component | Purpose |
|-----------|---------|
| Navigation Bar | Enables navigation between pages |
| Headings (`<h2>`, `<h3>`) | Display page titles |
| Paragraph (`<p>`) | Present project information |
| Form (`<form>`) | Collect user input |
| Labels (`<label>`) | Identify input fields |
| Text Inputs (`<input>`) | Accept agricultural parameters |
| Button (`<button>`) | Submit the prediction request |

---

## Workflow

The HTML interface performs the following operations:

1. Display the Home page.
2. Navigate to the About page for project information.
3. Open the FindYourCrop page.
4. Enter agricultural and environmental parameters.
5. Submit the form to the Flask backend.
6. Process the input using the trained machine learning model.
7. Display the recommended crop.

---

## Observations

The HTML pages provide the following functionalities:

- Simple and intuitive navigation.
- Clear presentation of project information.
- Efficient collection of agricultural parameters.
- Seamless integration with the Flask backend.
- Real-time crop recommendation display.

---

## Purpose

Building HTML pages helps to:

- Create an interactive user interface.
- Improve user experience.
- Enable communication between users and the prediction model.
- Support intelligent crop recommendation.
- Facilitate web application deployment.

---

## Expected Outcome

After completing this step:

- Users can easily navigate the application.
- Agricultural information can be entered through the prediction form.
- Input data is submitted successfully to the backend.
- Crop recommendations are displayed accurately.
- The web application provides an efficient and user-friendly experience.

---

## Conclusion

The HTML pages form the frontend of the **OptiCrop: Smart Agricultural Production Optimization Engine**. The Home page introduces the system, the About page explains its objectives, and the FindYourCrop page enables users to provide agricultural parameters for intelligent crop prediction. Together, these pages create a seamless and interactive interface that supports accurate crop recommendations and enhances the overall usability of the application.
