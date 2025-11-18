"""
Simple test script that can be run while the server is already running.
"""
import sys
sys.path.insert(0, '.')

from predict import predict_cervical_cancer_risk
import json

# Test data
test_patient = {
    'Age': 25,
    'Number of sexual partners': 2,
    'First sexual intercourse': 18,
    'Num of pregnancies': 1,
    'Smokes': 0,
    'Smokes (years)': 0.0,
    'Smokes (packs/year)': 0.0,
    'Hormonal Contraceptives': 1,
    'Hormonal Contraceptives (years)': 2.0,
    'IUD': 0,
    'IUD (years)': 0.0,
    'STDs': 0,
    'STDs (number)': 0,
    'STDs:condylomatosis': 0,
    'STDs:cervical condylomatosis': 0,
    'STDs:vaginal condylomatosis': 0,
    'STDs:vulvo-perineal condylomatosis': 0,
    'STDs:syphilis': 0,
    'STDs:pelvic inflammatory disease': 0,
    'STDs:genital herpes': 0,
    'STDs:molluscum contagiosum': 0,
    'STDs:AIDS': 0,
    'STDs:HIV': 0,
    'STDs:Hepatitis B': 0,
    'STDs:HPV': 0
}

print("=" * 60)
print("Testing Prediction Function Directly")
print("=" * 60)

try:
    result = predict_cervical_cancer_risk(test_patient)
    print("\n SUCCESS! Prediction completed:")
    print(f"  Risk Score: {result['risk_score']:.4f}")
    print(f"  Risk Level: {result['risk_level']}")
    print(f"  Recommendation: {result['recommendation']}")
    print(f"  Model Used: {result['model_used']}")
    print("\n" + "=" * 60)
    print(" The prediction function works correctly!")
    print("=" * 60)
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\nPlease ensure:")
    print("  1. Model files exist in ../model-training/models/")
    print("  2. All required packages are installed")
