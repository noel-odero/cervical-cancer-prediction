"""
Pydantic models for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional


class PredictionInput(BaseModel):
    """
    Input model for cervical cancer risk prediction.
    All fields have data type constraints and realistic range validations.
    """
    Age: int = Field(..., ge=15, le=100, description="Age of the patient (15-100 years)")
    Number_of_sexual_partners: int = Field(..., ge=0, le=50, description="Number of sexual partners (0-50)")
    First_sexual_intercourse: int = Field(..., ge=10, le=40, description="Age at first sexual intercourse (10-40 years)")
    Num_of_pregnancies: int = Field(..., ge=0, le=20, description="Number of pregnancies (0-20)")
    Smokes: int = Field(..., ge=0, le=1, description="Smoking status (0=No, 1=Yes)")
    Smokes_years: float = Field(..., ge=0, le=80, description="Years of smoking (0-80 years)")
    Smokes_packs_year: float = Field(..., ge=0, le=100, description="Packs per year (0-100)")
    Hormonal_Contraceptives: int = Field(..., ge=0, le=1, description="Hormonal contraceptives use (0=No, 1=Yes)")
    Hormonal_Contraceptives_years: float = Field(..., ge=0, le=50, description="Years using hormonal contraceptives (0-50)")
    IUD: int = Field(..., ge=0, le=1, description="IUD use (0=No, 1=Yes)")
    IUD_years: float = Field(..., ge=0, le=50, description="Years using IUD (0-50)")
    STDs: int = Field(..., ge=0, le=1, description="STDs status (0=No, 1=Yes)")
    STDs_number: int = Field(..., ge=0, le=20, description="Number of STDs (0-20)")
    STDs_condylomatosis: int = Field(..., ge=0, le=1, description="STDs condylomatosis (0=No, 1=Yes)")
    STDs_cervical_condylomatosis: int = Field(..., ge=0, le=1, description="STDs cervical condylomatosis (0=No, 1=Yes)")
    STDs_vaginal_condylomatosis: int = Field(..., ge=0, le=1, description="STDs vaginal condylomatosis (0=No, 1=Yes)")
    STDs_vulvo_perineal_condylomatosis: int = Field(..., ge=0, le=1, description="STDs vulvo-perineal condylomatosis (0=No, 1=Yes)")
    STDs_syphilis: int = Field(..., ge=0, le=1, description="STDs syphilis (0=No, 1=Yes)")
    STDs_pelvic_inflammatory_disease: int = Field(..., ge=0, le=1, description="STDs pelvic inflammatory disease (0=No, 1=Yes)")
    STDs_genital_herpes: int = Field(..., ge=0, le=1, description="STDs genital herpes (0=No, 1=Yes)")
    STDs_molluscum_contagiosum: int = Field(..., ge=0, le=1, description="STDs molluscum contagiosum (0=No, 1=Yes)")
    STDs_AIDS: int = Field(..., ge=0, le=1, description="STDs AIDS (0=No, 1=Yes)")
    STDs_HIV: int = Field(..., ge=0, le=1, description="STDs HIV (0=No, 1=Yes)")
    STDs_Hepatitis_B: int = Field(..., ge=0, le=1, description="STDs Hepatitis B (0=No, 1=Yes)")
    STDs_HPV: int = Field(..., ge=0, le=1, description="STDs HPV (0=No, 1=Yes)")

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 25,
                "Number_of_sexual_partners": 2,
                "First_sexual_intercourse": 18,
                "Num_of_pregnancies": 1,
                "Smokes": 0,
                "Smokes_years": 0.0,
                "Smokes_packs_year": 0.0,
                "Hormonal_Contraceptives": 1,
                "Hormonal_Contraceptives_years": 2.0,
                "IUD": 0,
                "IUD_years": 0.0,
                "STDs": 0,
                "STDs_number": 0,
                "STDs_condylomatosis": 0,
                "STDs_cervical_condylomatosis": 0,
                "STDs_vaginal_condylomatosis": 0,
                "STDs_vulvo_perineal_condylomatosis": 0,
                "STDs_syphilis": 0,
                "STDs_pelvic_inflammatory_disease": 0,
                "STDs_genital_herpes": 0,
                "STDs_molluscum_contagiosum": 0,
                "STDs_AIDS": 0,
                "STDs_HIV": 0,
                "STDs_Hepatitis_B": 0,
                "STDs_HPV": 0
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
                "model_used": "RandomForestRegressor"
            }
        }
    }
