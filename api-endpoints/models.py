"""
Pydantic models for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional


class PredictionInput(BaseModel):
    """Input model for cervical cancer risk prediction using the 10
    VIF-selected behavioral and STD-related features used to train the
    current LinearRegression model.
    """
    Number_of_sexual_partners: int = Field(
        ..., ge=0, le=50,
        description="Number of sexual partners (0-50)",
        alias="Number of sexual partners"
    )
    First_sexual_intercourse: int = Field(
        ..., ge=10, le=30,
        description="Age at first sexual intercourse (10-30)",
        alias="First sexual intercourse"
    )
    Smokes: int = Field(
        ..., ge=0, le=1,
        description="Smoking status (0=No, 1=Yes)"
    )
    Hormonal_Contraceptives: int = Field(
        ..., ge=0, le=1,
        description="Hormonal contraceptives usage (0=No, 1=Yes)",
        alias="Hormonal Contraceptives"
    )
    IUD_years: int = Field(
        ..., ge=0, le=20,
        description="Years of IUD usage (0-20)",
        alias="IUD (years)"
    )
    STDs: int = Field(
        ..., ge=0, le=1,
        description="History of any STD (0=No, 1=Yes)"
    )
    STDs_number: int = Field(
        ..., ge=0, le=10,
        description="Total number of diagnosed STDs (0-10)",
        alias="STDs (number)"
    )
    STDs_cervical_condylomatosis: int = Field(
        ..., ge=0, le=1,
        description="Cervical condylomatosis history (0=No, 1=Yes)",
        alias="STDs:cervical condylomatosis"
    )
    STDs_pelvic_inflammatory_disease: int = Field(
        ..., ge=0, le=1,
        description="Pelvic inflammatory disease history (0=No, 1=Yes)",
        alias="STDs:pelvic inflammatory disease"
    )
    STDs_genital_herpes: int = Field(
        ..., ge=0, le=1,
        description="Genital herpes history (0=No, 1=Yes)",
        alias="STDs:genital herpes"
    )

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "example": {
                "Number of sexual partners": 3,
                "First sexual intercourse": 17,
                "Smokes": 0,
                "Hormonal Contraceptives": 1,
                "IUD (years)": 0,
                "STDs": 0,
                "STDs (number)": 0,
                "STDs:cervical condylomatosis": 0,
                "STDs:pelvic inflammatory disease": 0,
                "STDs:genital herpes": 0
            }
        }
    }


class PredictionOutput(BaseModel):
    """Output model for cervical cancer risk prediction response."""
    risk_score: float = Field(..., description="Continuous risk score clipped to 0.0 - 1.0")
    risk_level: str = Field(..., description="Risk category: LOW, MODERATE, HIGH, or VERY HIGH (LinearRegression thresholds)")
    recommendation: str = Field(..., description="Recommendation based on risk level")
    model_used: str = Field(..., description="Name of the ML model used for prediction")

    model_config = {
        "protected_namespaces": (),
        "json_schema_extra": {
            "example": {
                "risk_score": 0.045,
                "risk_level": "LOW",
                "recommendation": "Routine screening recommended",
                "model_used": "LinearRegression"
            }
        }
    }
