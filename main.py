from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import pickle
import pandas as pd


# Create FastAPI app
app = FastAPI()


# Load trained ML model
model = pickle.load(open("model.pkl", "rb"))


# Templates folder
templates = Jinja2Templates(directory="templates")


# Static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


# ---------------- HOME PAGE ----------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="index.html"

    )


# ---------------- PREDICTION ROUTE ----------------

@app.post("/predict_form", response_class=HTMLResponse)
def predict_form(

    request: Request,

    age: float = Form(...),

    is_female: int = Form(...),

    bmi: float = Form(...),

    children: float = Form(...),

    is_smoker: int = Form(...),

    region_southeast: int = Form(...),

    bmi_category_obese: int = Form(...)

):


    # Create dataframe from user input
    data = pd.DataFrame([{

        'age': age,

        'is_female': is_female,

        'bmi': bmi,

        'children': children,

        'is_smoker': is_smoker,

        'region_southeast': region_southeast,

        'bmi_category_obese': bmi_category_obese

    }])


    # Predict insurance charges
    prediction = model.predict(data)


    # Return prediction to frontend
    return templates.TemplateResponse(

        request=request,

        name="index.html",

        context={

            "prediction": round(float(prediction[0]), 2)

        }

    )