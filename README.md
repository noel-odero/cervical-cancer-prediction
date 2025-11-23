# Cervical Cancer Risk Prediction System

Complete end-to-end machine learning system for predicting cervical cancer risk based on patient risk factors.

## Project Overview

This project consists of two main components:
1. **Model Training** (Task 1): ML model development and evaluation
2. **API Backend** (Task 2): FastAPI deployment for predictions

## Problem Statement
Delayed or inaccessible cervical cancer risk assessment leads to missed early detection and poorer patient outcomes.

## Mission Statement
Provide a fast, accessible, privacy‑respecting Flutter app that uses a validated prediction API to deliver actionable cervical cancer risk scores and screening recommendations.

## Dataset

- **Source**: [Kaggle](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification)
- **Features**: 36 risk factors including age, sexual history, STDs, contraceptive use
- **Target**: Cervical cancer risk score (0-1 continuous value)
- **Samples**: 858 patients

## Mobile app 
- [Link to the frontend Repo](https://github.com/noel-odero/cervical-cancer-prediction-frontend)
- [Link to the deployed frontend](https://cervical-cancer-predictt.netlify.app/)
- [Link to the demo video](https://www.loom.com/share/248b46762cd14e46a1f13d700775bb97)


## Quick Start

### 1. Model Training
```bash
cd 01-model-training
jupyter notebook notebook.ipynb
```

### 2. Run API Locally
```bash
cd 02-api
pip install -r requirements.txt
uvicorn main:app --reload
# Visit: http://localhost:8000/docs
```


## Live Deployment

- **API Endpoint**: https://cervical-cancer-prediction.onrender.com
- **API Documentation**: https://cervical-cancer-prediction.onrender.com/docs

## Project Structure
```
├── 01-model-training/    # Jupyter notebook, dataset, trained models
├── 02-api/               # FastAPI backend application

```

## Technologies Used

- **ML**: Python, scikit-learn, pandas, numpy
- **API**: FastAPI, Pydantic, Uvicorn
- **Deployment**: Render (API)

## Model Performance

| Model | RMSE | R² Score |
|-------|------|----------|
| Linear Regression | 0.230038 | -0.004152 |
| Random Forest | 0.244282 | -0.132359 |
| Decision Tree | 0.308643 | -0.807647 |


**Best Model**: Linear Regression (RMSE: 0.230038)

## Author

Noel Odero - [GitHub Profile](https://github.com/noel-odero)





