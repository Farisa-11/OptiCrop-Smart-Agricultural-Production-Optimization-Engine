# Entity Relationship Diagram

## Overview

The ER diagram represents the core entities involved in the **OptiCrop: Smart Agricultural Production Optimization Engine** and illustrates how they interact with one another. It provides a structured database design for managing soil data, crop recommendations, machine learning models, prediction results, and generated reports.

---

## Entities Involved

The system consists of the following seven primary entities:

1. User
2. SoilData
3. Crop
4. Dataset
5. MLModel
6. Prediction
7. Report

---

## Primary Keys

| Entity | Primary Key |
|----------|------------|
| User | `user_id` |
| SoilData | `soil_id` |
| Crop | `crop_id` |
| Dataset | `dataset_id` |
| MLModel | `model_id` |
| Prediction | `prediction_id` |
| Report | `report_id` |

---

## Relationships

### User → SoilData
- One user can submit multiple soil data records.
- **Relationship:** One-to-Many (1:M)

### SoilData → Prediction
- Each soil data record generates one prediction.
- **Relationship:** One-to-One (1:1)

### Crop → Prediction
- A crop can be recommended in multiple prediction results.
- **Relationship:** One-to-Many (1:M)

### Dataset → MLModel
- A dataset can be used to train multiple machine learning models.
- **Relationship:** One-to-Many (1:M)

### MLModel → Prediction
- One machine learning model can generate multiple prediction records.
- **Relationship:** One-to-Many (1:M)

### Prediction → Report
- One prediction can generate multiple reports and recommendations.
- **Relationship:** One-to-Many (1:M)

---

## Foreign Keys

### SoilData
- `user_id` → `User.user_id`

### MLModel
- `dataset_id` → `Dataset.dataset_id`

### Prediction
- `soil_id` → `SoilData.soil_id`
- `crop_id` → `Crop.crop_id`
- `model_id` → `MLModel.model_id`

### Report
- `prediction_id` → `Prediction.prediction_id`

---

## Cardinality

- A user can submit multiple soil data records.
- Each soil data record generates one crop prediction.
- A crop can appear in multiple prediction records.
- A dataset can train multiple machine learning models.
- A machine learning model can generate predictions for many users and different soil conditions.
- Each prediction can generate one or more reports containing recommendations and insights.

---

## Normalization and Structure

The database is normalized by separating:

- User information
- Soil and environmental data
- Crop information
- Datasets
- Machine learning models
- Prediction records
- Reports

This normalization reduces data redundancy, improves scalability, maintains referential integrity, and supports efficient data management.

---

## Use Case Coverage

The ER model supports:

- Collecting and managing soil and environmental data
- Managing agricultural datasets
- Training machine learning models
- Predicting suitable crops
- Generating crop recommendations
- Producing analytical reports
- Supporting data-driven agricultural decision-making
