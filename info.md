# Insurance Charges Prediction App - Complete Working Process

This project is a Machine Learning web application that predicts medical insurance charges based on user information such as age, BMI, smoking status, gender, and region.

---

# Complete Flow of the Application

```text
User Opens Website
        ↓
Frontend Form Takes Input
        ↓
FastAPI Receives Data
        ↓
Data Converted into DataFrame
        ↓
Trained ML Model Loaded from model.pkl
        ↓
Model Predicts Insurance Charges
        ↓
Prediction Sent Back to Frontend
        ↓
Result Displayed on Website
```

---

# Technologies Used

## Frontend
- HTML
- CSS

Frontend is used to:
- create user interface
- take user input
- display prediction result

---

## Backend
- FastAPI

Backend is used to:
- receive form data
- process input
- connect frontend with ML model
- return prediction result

---

## Machine Learning
- Scikit-learn
- Linear Regression

Machine Learning model is used to:
- learn patterns from dataset
- predict insurance charges

---

# How the Model Was Created

## Step 1 - Dataset Loading

Dataset contains:
- age
- gender
- bmi
- children
- smoker
- region
- insurance charges

Dataset was loaded using Pandas.

```python
df = pd.read_csv("insurance.csv")
```

---

## Step 2 - Data Preprocessing

Categorical values were converted into numerical values because ML models only understand numbers.

Example:

```text
male → 0
female → 1
```

---

## Step 3 - Feature Selection

Input features:

```text
age
is_female
bmi
children
is_smoker
region_southeast
bmi_category_obese
```

Target column:

```text
charges
```

---

## Step 4 - Train Test Split

Dataset was divided into:

```text
Training Data → 67%
Testing Data → 33%
```

Purpose:
- Training data teaches model
- Testing data checks performance

---

## Step 5 - Model Training

Linear Regression model was trained.

```python
model = LinearRegression()

model.fit(x_train, y_train)
```

Model learns relationship between:
- user features
- insurance charges

---

# What is Linear Regression?

Linear Regression is a supervised Machine Learning algorithm used for predicting continuous numerical values.

In this project:
- Input = user information
- Output = insurance charges

Linear Regression tries to find the best-fit mathematical relationship between inputs and output.

Equation:

```text
y = mx + b
```

Where:
- y = predicted value
- x = input features
- m = slope/weight
- b = intercept

---

# Model Evaluation

Two evaluation metrics were used:

## R² Score

Measures accuracy of model.

```text
R² Score = 0.77
```

Meaning:
- model predicts approximately 77% correctly

---

## Mean Squared Error (MSE)

Measures average prediction error.

Lower value means better model.

---

# What is model.pkl?

`model.pkl` is a saved trained Machine Learning model.

It is created using Python Pickle library.

---

# Why model.pkl is Important

Without `model.pkl`:

```text
Every time app starts:
→ retrain model again
→ slow application
```

With `model.pkl`:

```text
Train once
Save model
Load anytime
Predict instantly
```

---

# How model.pkl is Created

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

Meaning:
- save trained model permanently

---

# How model.pkl is Loaded

```python
model = pickle.load(open("model.pkl", "rb"))
```

Meaning:
- load saved model into memory
- use it for prediction

---

# How FastAPI Works in This Project

FastAPI acts as the backend server.

It:
- receives data from frontend
- sends data to ML model
- returns prediction result

---

# Main Routes in FastAPI

## Home Route

```python
@app.get("/")
```

Purpose:
- opens website homepage

---

## Prediction Route

```python
@app.post("/predict_form")
```

Purpose:
- receives form data
- predicts insurance charges
- sends result back

---

# How Prediction Happens

## Step 1

User enters data in form.

Example:

```text
Age = 25
BMI = 27.9
Smoker = Yes
```

---

## Step 2

Form sends data to backend.

```html
<form action="/predict_form" method="post">
```

---

## Step 3

FastAPI receives data.

```python
age: float = Form(...)
```

---

## Step 4

Data converted into DataFrame.

```python
data = pd.DataFrame([...])
```

---

## Step 5

ML model predicts.

```python
prediction = model.predict(data)
```

---

## Step 6

Prediction displayed on website.

```text
Predicted Insurance Charges = ₹130079
```

---

# Frontend Working

Frontend contains:
- input fields
- dropdown menus
- predict button
- clear form button

HTML creates structure.

CSS adds:
- styling
- responsiveness
- animations
- layout

---

# Deployment Process

Application was deployed using Render.

---

# Why Deployment is Needed

Without deployment:
- app runs only on local computer

After deployment:
- app accessible from anywhere on internet

---

# Deployment Flow

```text
Local Project
      ↓
GitHub Repository
      ↓
Render Deployment
      ↓
Public Website URL
```

---

# GitHub Role

GitHub stores:
- source code
- frontend files
- backend files
- model.pkl

Render automatically fetches latest code from GitHub.

---

# Render Role

Render:
- hosts application online
- runs FastAPI server
- provides public URL

---

# Start Command Used on Render

```text
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# Final Project Architecture

```text
Frontend (HTML/CSS)
        ↓
FastAPI Backend
        ↓
model.pkl (ML Model)
        ↓
Prediction
        ↓
Frontend Result
```

---

# Skills Demonstrated

- Machine Learning
- Linear Regression
- Data Preprocessing
- FastAPI
- API Development
- HTML/CSS
- Deployment
- GitHub
- Render
- Model Serialization using Pickle

---

# Conclusion

This project demonstrates a complete end-to-end Machine Learning deployment pipeline.

The application:
- trains ML model
- saves model
- builds API
- creates frontend
- deploys application online

Users can now predict insurance charges directly through the deployed website.
