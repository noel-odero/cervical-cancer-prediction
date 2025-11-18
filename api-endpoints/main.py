"""
FastAPI application for Cervical Cancer Risk Prediction API.
This API provides endpoints for predicting cervical cancer risk based on patient data.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from models import PredictionInput, PredictionOutput
from predict import predict_cervical_cancer_risk
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Cervical Cancer Risk Prediction API",
    description="API for predicting cervical cancer risk using machine learning models",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root endpoint - provides API information.
    """
    return {
        "message": "Welcome to Cervical Cancer Risk Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {
        "status": "healthy",
        "service": "Cervical Cancer Risk Prediction API"
    }


@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    """
    POST endpoint for cervical cancer risk prediction.
    
    Args:
        input_data (PredictionInput): Patient data with all required risk factors.
        
    Returns:
        PredictionOutput: Prediction results including risk score, level, and recommendations.
        
    Raises:
        HTTPException: If prediction fails due to invalid input or model errors.
    """
    try:
        # Convert Pydantic model to dictionary
        input_dict = input_data.model_dump()
        
        logger.info(f"Received prediction request with Age: {input_dict.get('Age')}")
        
        # Make prediction
        result = predict_cervical_cancer_risk(input_dict)
        
        logger.info(f"Prediction successful: Risk Level = {result['risk_level']}")
        
        return PredictionOutput(**result)
    
    except FileNotFoundError as e:
        logger.error(f"Model files not found: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Model files not found. Please ensure the model is trained and saved."
        )
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler for unexpected errors.
    """
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred. Please try again later."
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
