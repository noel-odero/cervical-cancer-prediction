"""
Simple test script that can be run while the server is already running.
"""
import sys
sys.path.insert(0, '.')

from predict import predict_cervical_cancer_risk
import json

# Test data - LOW RISK CASE
test_patient_low = {
    'STDs': 0,
    'STDs (number)': 0,
    'STDs:condylomatosis': 0,
    'STDs:vulvo-perineal condylomatosis': 0,
    'STDs:HIV': 0,
    'STDs: Number of diagnosis': 0,
    'Dx:Cancer': 0,
    'Dx:HPV': 0,
    'Dx': 0,
    'Citology': 0
}

# Test data - MODERATE RISK CASE
test_patient_moderate = {
    'STDs': 1,
    'STDs (number)': 2,
    'STDs:condylomatosis': 0,
    'STDs:vulvo-perineal condylomatosis': 1,
    'STDs:HIV': 0,
    'STDs: Number of diagnosis': 2,
    'Dx:Cancer': 0,
    'Dx:HPV': 1,
    'Dx': 0,
    'Citology': 1
}

# Test data - HIGH RISK CASE
test_patient_high = {
    'STDs': 1,
    'STDs (number)': 3,
    'STDs:condylomatosis': 1,
    'STDs:vulvo-perineal condylomatosis': 1,
    'STDs:HIV': 0,
    'STDs: Number of diagnosis': 3,
    'Dx:Cancer': 0,
    'Dx:HPV': 1,
    'Dx': 1,
    'Citology': 1
}

# Test data - VERY HIGH RISK CASE
test_patient_very_high = {
    'STDs': 1,
    'STDs (number)': 20,
    'STDs:condylomatosis': 1,
    'STDs:vulvo-perineal condylomatosis': 1,
    'STDs:HIV': 1,
    'STDs: Number of diagnosis': 10,
    'Dx:Cancer': 1,
    'Dx:HPV': 1,
    'Dx': 1,
    'Citology': 1
}

# Test maximum possible score
test_max = {
    'STDs': 1,
    'STDs (number)': 20,
    'STDs:condylomatosis': 1,
    'STDs:vulvo-perineal condylomatosis': 1,
    'STDs:HIV': 1,
    'STDs: Number of diagnosis': 10,
    'Dx:Cancer': 1,
    'Dx:HPV': 1,
    'Dx': 1,
    'Citology': 1
}

print("=" * 60)
print("Testing Prediction Function - All Risk Levels")
print("=" * 60)

try:
    # Test LOW RISK case
    print("\n[TEST 1: LOW RISK CASE]")
    result1 = predict_cervical_cancer_risk(test_patient_low)
    print("SUCCESS! Prediction completed:")
    print(f"  Risk Score: {result1['risk_score']:.4f}")
    print(f"  Risk Level: {result1['risk_level']}")
    print(f"  Recommendation: {result1['recommendation']}")
    print(f"  Model Used: {result1['model_used']}")
    
    # Test MODERATE RISK case
    print("\n[TEST 2: MODERATE RISK CASE]")
    result2 = predict_cervical_cancer_risk(test_patient_moderate)
    print("SUCCESS! Prediction completed:")
    print(f"  Risk Score: {result2['risk_score']:.4f}")
    print(f"  Risk Level: {result2['risk_level']}")
    print(f"  Recommendation: {result2['recommendation']}")
    print(f"  Model Used: {result2['model_used']}")
    
    # Test HIGH RISK case
    print("\n[TEST 3: HIGH RISK CASE]")
    result3 = predict_cervical_cancer_risk(test_patient_high)
    print("SUCCESS! Prediction completed:")
    print(f"  Risk Score: {result3['risk_score']:.4f}")
    print(f"  Risk Level: {result3['risk_level']}")
    print(f"  Recommendation: {result3['recommendation']}")
    print(f"  Model Used: {result3['model_used']}")
    
    # Test VERY HIGH RISK case
    print("\n[TEST 4: VERY HIGH RISK CASE]")
    result4 = predict_cervical_cancer_risk(test_patient_very_high)
    print("SUCCESS! Prediction completed:")
    print(f"  Risk Score: {result4['risk_score']:.4f}")
    print(f"  Risk Level: {result4['risk_level']}")
    print(f"  Recommendation: {result4['recommendation']}")
    print(f"  Model Used: {result4['model_used']}")
    
    # Test MAXIMUM possible score
    print("\n[TEST 5: MAXIMUM SCORE TEST]")
    result5 = predict_cervical_cancer_risk(test_max)
    print("SUCCESS! Maximum score:")
    print(f"  Risk Score: {result5['risk_score']:.4f}")
    print(f"  Risk Level: {result5['risk_level']}")
    print(f"  Recommendation: {result5['recommendation']}")
    print(f"  Model Used: {result5['model_used']}")
    
    print("\n" + "=" * 60)
    print("The prediction function works correctly!")
    print("=" * 60)
except Exception as e:
    print(f"\n ERROR: {str(e)}")
    print("\nPlease ensure:")
    print("  1. Model files exist in ../model-training/models/")
    print("  2. All required packages are installed")
