import os
import joblib
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from .forms import ChurnForm

# Define base path to models folder
BASE_DIR = settings.BASE_DIR

# Load trained model, scaler, and expected columns
model = joblib.load(os.path.join(BASE_DIR, "models", "churn_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))
model_columns = joblib.load(os.path.join(BASE_DIR, "models", "model_columns.pkl"))

def churn_predict(request):
    prediction = None
    probability = None

    if request.method == 'POST':
        form = ChurnForm(request.POST)
        if form.is_valid():
            # Build input dictionary from form
            input_dict = {
                'gender': form.cleaned_data['gender'],
                'SeniorCitizen': form.cleaned_data['SeniorCitizen'],
                'Partner': form.cleaned_data['Partner'],
                'tenure': form.cleaned_data['tenure'],
                'MonthlyCharges': form.cleaned_data['MonthlyCharges'],
                'TotalCharges': form.cleaned_data['TotalCharges'],
                'InternetService': form.cleaned_data['InternetService'],
                'Contract': form.cleaned_data['Contract'],
            }

            # Convert to DataFrame
            input_df = pd.DataFrame([input_dict])

            # One-hot encode categorical features
            input_encoded = pd.get_dummies(input_df)

            # Add any missing columns from model_columns
            for col in model_columns:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0

            # Add engagement_score feature (same logic as training)
            input_encoded['engagement_score'] = input_encoded['tenure'] * input_encoded['MonthlyCharges']

            # Ensure column order matches what model expects
            input_encoded = input_encoded[model_columns]

            # Scale numerical columns
            numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
            input_encoded[numerical_cols] = scaler.transform(input_encoded[numerical_cols])

            # Make prediction
            prediction = model.predict(input_encoded)[0]
            probability = model.predict_proba(input_encoded)[0][1]

            return render(request, 'churn_app/result.html', {
                'prediction': prediction,
                'probability': round(probability * 100, 2) if probability is not None else None
            })

    else:
        form = ChurnForm()

    return render(request, 'churn_app/form.html', {'form': form})


def churn_dashboard(request):
    return render(request, 'churn_app/dashboard.html')
