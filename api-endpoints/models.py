"""
Pydantic models for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional


class PredictionInput(BaseModel):
    """
    Input model for cervical cancer risk prediction.
    All fields have data type constraints and realistic range validations.
    These are the exact 10 features used to train the DecisionTreeRegressor model.
    """
    STDs: int = Field(..., ge=0, le=1, description="STDs status (0=No, 1=Yes)")
    STDs_number: int = Field(..., ge=0, le=20, description="Number of STDs (0-20)", alias="STDs (number)")
    STDs_condylomatosis: int = Field(..., ge=0, le=1, description="STDs condylomatosis (0=No, 1=Yes)", alias="STDs:condylomatosis")
    STDs_vulvo_perineal_condylomatosis: int = Field(..., ge=0, le=1, description="STDs vulvo-perineal condylomatosis (0=No, 1=Yes)", alias="STDs:vulvo-perineal condylomatosis")
    STDs_HIV: int = Field(..., ge=0, le=1, description="STDs HIV (0=No, 1=Yes)", alias="STDs:HIV")
    STDs_Number_of_diagnosis: int = Field(..., ge=0, le=10, description="Number of STD diagnoses (0-10)", alias="STDs: Number of diagnosis")
    Dx_Cancer: int = Field(..., ge=0, le=1, description="Cancer diagnosis (0=No, 1=Yes)", alias="Dx:Cancer")
    Dx_HPV: int = Field(..., ge=0, le=1, description="HPV diagnosis (0=No, 1=Yes)", alias="Dx:HPV")
    Dx: int = Field(..., ge=0, le=1, description="Diagnosis (0=No, 1=Yes)")
    Citology: int = Field(..., ge=0, le=1, description="Cytology test result (0=No, 1=Yes)")

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "STDs": 0,
                "STDs (number)": 0,
                "STDs:condylomatosis": 0,
                "STDs:vulvo-perineal condylomatosis": 0,
                "STDs:HIV": 0,
                "STDs: Number of diagnosis": 0,
                "Dx:Cancer": 0,
                "Dx:HPV": 0,
                "Dx": 0,
                "Citology": 0
            }
        }
    }


class PredictionOutput(BaseModel):
    """
    Output model for cervical cancer risk prediction response.
    """
    risk_score: float = Field(..., description="Continuous risk score (0.0 - 1.0)")
    risk_level: str = Field(..., description="Risk category: LOW, MODERATE, HIGH, or VERY HIGH")
    recommendation: str = Field(..., description="Medical recommendation based on risk level")
    model_used: str = Field(..., description="Name of the ML model used for prediction")

    model_config = {
        "protected_namespaces": (),
        "json_schema_extra": {
            "example": {
                "risk_score": 0.15,
                "risk_level": "LOW",
                "recommendation": "Routine screening recommended",
                "model_used": "DecisionTreeRegressor"
            }
        }
    }
