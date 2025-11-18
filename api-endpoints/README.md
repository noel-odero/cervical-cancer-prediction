# Cervical Cancer Risk Prediction API

A FastAPI-based REST API for predicting cervical cancer risk using machine learning models.

## 🚀 Features

- **POST /predict** - Make risk predictions based on patient data
- **GET /health** - Health check endpoint
- **GET /docs** - Interactive Swagger UI documentation
- **CORS Support** - Cross-Origin Resource Sharing enabled
- **Input Validation** - Pydantic models with range constraints
- **Data Type Enforcement** - Strict type checking for all inputs

## 📋 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic
- scikit-learn
- pandas
- numpy
- joblib

See `requirements.txt` for specific versions.

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/noel-odero/cervical-cancer-prediction.git
cd cervical-cancer-prediction/api-endpoints
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Ensure model files exist**
Make sure the following files are in `../model-training/models/`:
- `best_model.pkl`
- `preprocessor.pkl`
- `feature_list.pkl`

## 🏃 Running Locally

### Start the server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Access the API
- **API Base URL**: http://localhost:8000
- **Swagger UI Documentation**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🧪 Testing

Run the test suite:
```bash
python test_api.py
```

Or test manually using curl:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d @../model-training/models/example_input.json
```

## 📡 API Endpoints

### POST /predict

Predict cervical cancer risk for a patient.

**Request Body:**
```json
{
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
```

**Response:**
```json
{
  "risk_score": 0.15,
  "risk_level": "LOW",
  "recommendation": "Routine screening recommended",
  "model_used": "RandomForestRegressor"
}
```

**Risk Levels:**
- **LOW** (0.0 - 0.2): Routine screening recommended
- **MODERATE** (0.2 - 0.5): Consider additional screening and consultation
- **HIGH** (0.5 - 0.7): Consult healthcare provider soon for evaluation
- **VERY HIGH** (0.7 - 1.0): Immediate medical intervention required

## 🌐 Deployment on Render

### Step 1: Prepare Repository
Ensure your repository has:
- `api-endpoints/main.py`
- `api-endpoints/models.py`
- `api-endpoints/predict.py`
- `api-endpoints/requirements.txt`
- `model-training/models/` (with .pkl files)

### Step 2: Create Render Account
1. Go to [Render.com](https://render.com/)
2. Sign up or log in with GitHub

### Step 3: Deploy Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure settings:
   - **Name**: `cervical-cancer-api`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: `api-endpoints`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: Free (or paid for better performance)

4. Click **"Create Web Service"**

### Step 4: Environment Variables (Optional)
Add any needed environment variables in Render dashboard.

### Step 5: Access Your API
After deployment, Render provides a URL like:
```
https://cervical-cancer-api-xxxx.onrender.com
```

Access the Swagger UI:
```
https://cervical-cancer-api-xxxx.onrender.com/docs
```

## 📝 Input Validation

All inputs are validated with:
- **Type checking**: Integer, float, or string as specified
- **Range constraints**: Values must fall within realistic bounds
- **Required fields**: All patient risk factors must be provided

### Validation Examples

**Valid Input:**
```json
{
  "Age": 25,  // 15-100
  "Number_of_sexual_partners": 2,  // 0-50
  "Smokes": 0  // 0 or 1
}
```

**Invalid Input (returns 422 Validation Error):**
```json
{
  "Age": 150,  // Outside range
  "Number_of_sexual_partners": -5,  // Negative
  "Smokes": 2  // Not 0 or 1
}
```

## 🔒 CORS Configuration

CORS is configured to allow all origins. For production, update in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-domain.com"],  # Specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🐛 Troubleshooting

### Model files not found
```
Error: Model files not found. Please ensure the model is trained and saved.
```
**Solution**: Ensure `best_model.pkl`, `preprocessor.pkl`, and `feature_list.pkl` exist in `../model-training/models/`

### Import errors
```
ModuleNotFoundError: No module named 'fastapi'
```
**Solution**: Install dependencies: `pip install -r requirements.txt`

### Port already in use
```
Error: Address already in use
```
**Solution**: Use a different port: `uvicorn main:app --port 8001`

## 📊 Project Structure

```
api-endpoints/
├── main.py              # FastAPI application
├── models.py            # Pydantic models for validation
├── predict.py           # Prediction logic
├── requirements.txt     # Python dependencies
├── test_api.py         # Test suite
└── README.md           # This file

model-training/
└── models/
    ├── best_model.pkl       # Trained ML model
    ├── preprocessor.pkl     # Data preprocessor
    ├── feature_list.pkl     # Feature names
    └── example_input.json   # Sample input
```

## 📚 Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **GitHub**: https://github.com/noel-odero/cervical-cancer-prediction

## 👨‍💻 Development

### Adding new endpoints
1. Define Pydantic models in `models.py`
2. Add endpoint function in `main.py`
3. Test using `test_api.py`

### Updating the model
1. Retrain in `model-training/Model.ipynb`
2. Save new `.pkl` files to `model-training/models/`
3. Restart the API server

## 📄 License

This project is part of an academic assignment.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📧 Contact

For questions or issues, please contact the repository owner.
