# Cervical Cancer Risk Prediction System

Complete end-to-end machine learning system for predicting cervical cancer risk based on patient risk factors.

## Project Overview

This project consists of three main components:
1. **Model Training** (Task 1): ML model development and evaluation
2. **API Backend** (Task 2): FastAPI deployment for predictions
3. **Web Interface** (Task 3): User-friendly frontend application

## Dataset

- **Source**: [Kaggle](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification)
- **Features**: 36 risk factors including age, sexual history, STDs, contraceptive use
- **Target**: Cervical cancer risk score (0-1 continuous value)
- **Samples**: 858 patients

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
- **Deployment**: Render (API), Netlify/Vercel (Frontend)

## Model Performance

| Model | RMSE | R² Score |
|-------|------|----------|
| Linear Regression | 0.2025 | 0.654 |
| SGD Regressor | 0.2018 | 0.658 |
| Decision Tree | 0.1876 | 0.712 |
| Random Forest | 0.1923 | 0.695 |

**Best Model**: Decision Tree (RMSE: 0.1876)

## Author

Noel Odero - [GitHub Profile](https://github.com/noel-odero)

