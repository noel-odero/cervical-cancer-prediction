"""
Prediction logic for cervical cancer risk assessment.
This module contains the prediction function extracted from the trained model.
"""
import joblib
import pandas as pd
import numpy as np
from pathlib import Path


def predict_cervical_cancer_risk(input_data_dict: dict) -> dict:
    """
    Prediction function for cervical cancer risk assessment.

    Args:
        input_data_dict (dict): A dictionary containing patient risk factors.

    Returns:
        dict: Prediction results containing:
            - risk_score (float): Continuous risk score (0.0 - 1.0)
            - risk_level (str): Risk category (LOW, MODERATE, HIGH, VERY HIGH)
            - recommendation (str): Medical recommendation
            - model_used (str): Name of the ML model used
    """
    
    # Define the path to model artifacts
    # Adjust path to point to model-training/models directory
    models_dir = Path(__file__).parent.parent / "model-training" / "models"
    
    # Load saved model artifacts
    model = joblib.load(models_dir / "best_model.pkl")
    preprocessor = joblib.load(models_dir / "preprocessor.pkl")
    feature_list = joblib.load(models_dir / "feature_list.pkl")
    
    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_data_dict])
    
    # Ensure all required features are present (fill missing with 0)
    for feature in feature_list:
        if feature not in input_df.columns:
            input_df[feature] = 0
    
    # Select only features used during training
    input_df = input_df[feature_list]
    
    # Apply preprocessing
    input_transformed = preprocessor.transform(input_df)
    
    # Make prediction
    risk_score = float(model.predict(input_transformed)[0])
    
    # Debug: Print the raw prediction
    print(f"DEBUG - Raw model prediction: {risk_score}")
    print(f"DEBUG - Input features: {input_data_dict}")
    
    # Clip risk score to valid range [0, 1]
    risk_score = np.clip(risk_score, 0.0, 1.0)
    
    # Interpret risk level based on score
    # Adjusted thresholds based on DecisionTree model output range (0.0 - 0.8)
    if risk_score < 0.15:
        risk_level = "LOW"
        recommendation = "Routine screening recommended"
    elif risk_score < 0.4:
        risk_level = "MODERATE"
        recommendation = "Consider additional screening and consultation"
    elif risk_score < 0.65:
        risk_level = "HIGH"
        recommendation = "Consult healthcare provider soon for evaluation"
    else:
        risk_level = "VERY HIGH"
        recommendation = "Immediate medical intervention required"
    
    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "recommendation": recommendation,
        "model_used": type(model).__name__
    }
