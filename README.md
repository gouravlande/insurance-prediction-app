# Insurance Charges Prediction App

A Machine Learning web application built using FastAPI and Linear Regression to predict medical insurance charges based on user details such as age, BMI, smoking status, gender, and region.

---

# Features

- Data preprocessing and feature engineering
- Linear Regression model training
- Model evaluation using R² Score and MSE
- FastAPI backend integration
- HTML/CSS frontend
- Real-time insurance charge prediction
- Swagger API documentation
- Deployable on Render

---

# Tech Stack

## Backend
- Python
- FastAPI

## Machine Learning
- Scikit-learn
- Pandas
- NumPy

## Frontend
- HTML
- CSS

## Deployment
- Render
- GitHub

---

# Project Structure

```text
insurance_prediction_project/
│
├── data/
│   └── insurance (1).csv
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── venv/
│
├── model.pkl
├── main.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

# Dataset Information

The dataset contains:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region
- Insurance Charges

---

# Machine Learning Workflow

```text
Dataset
   ↓
EDA
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Encoding
   ↓
Train-Test Split
   ↓
Linear Regression Model
   ↓
Evaluation
   ↓
Model Saving (model.pkl)
   ↓
FastAPI Deployment
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/gouravlande/insurance-prediction-app.git
```

---

## Navigate to Project

```bash
cd insurance-prediction-app
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn main:app --reload
```

---

# Open in Browser

```text
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Sample Prediction Inputs

| Feature | Value |
|---|---|
| Age | 25 |
| Female | 1 |
| BMI | 27.9 |
| Children | 0 |
| Smoker | 1 |
| Southeast | 0 |
| Obese | 0 |

---

# Model Performance

- R² Score: 0.77
- Mean Squared Error: 38488745.88

---

# Future Improvements

- Add multiple ML algorithms
- Improve UI design
- Deploy using Docker
- Add authentication
- Use advanced regression models

---

# Author

Gourav Lande

---

# License

This project is for educational and learning purposes.
