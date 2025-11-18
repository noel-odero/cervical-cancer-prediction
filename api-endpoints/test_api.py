"""
Test script for the Cervical Cancer Risk Prediction API.
Run this after starting the API server to verify it works correctly.
"""
import requests
import json

# API endpoint
API_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{API_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200


def test_prediction():
    """Test the prediction endpoint with sample data"""
    print("\n=== Testing Prediction Endpoint ===")
    
    # Sample patient data
    test_data = {
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
    
    print(f"Input Data: {json.dumps(test_data, indent=2)}")
    
    response = requests.post(f"{API_URL}/predict", json=test_data)
    print(f"\nStatus Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n🔍 Prediction Results:")
        print(f"  Risk Score: {result['risk_score']:.4f}")
        print(f"  Risk Level: {result['risk_level']}")
        print(f"  Recommendation: {result['recommendation']}")
        print(f"  Model Used: {result['model_used']}")
        return True
    else:
        print(f"Error: {response.text}")
        return False


def test_high_risk_case():
    """Test with a high-risk profile"""
    print("\n=== Testing High-Risk Profile ===")
    
    high_risk_data = {
        "Age": 45,
        "Number_of_sexual_partners": 10,
        "First_sexual_intercourse": 14,
        "Num_of_pregnancies": 5,
        "Smokes": 1,
        "Smokes_years": 20.0,
        "Smokes_packs_year": 15.0,
        "Hormonal_Contraceptives": 1,
        "Hormonal_Contraceptives_years": 15.0,
        "IUD": 1,
        "IUD_years": 10.0,
        "STDs": 1,
        "STDs_number": 3,
        "STDs_condylomatosis": 1,
        "STDs_cervical_condylomatosis": 0,
        "STDs_vaginal_condylomatosis": 0,
        "STDs_vulvo_perineal_condylomatosis": 0,
        "STDs_syphilis": 0,
        "STDs_pelvic_inflammatory_disease": 1,
        "STDs_genital_herpes": 1,
        "STDs_molluscum_contagiosum": 0,
        "STDs_AIDS": 0,
        "STDs_HIV": 0,
        "STDs_Hepatitis_B": 0,
        "STDs_HPV": 1
    }
    
    response = requests.post(f"{API_URL}/predict", json=high_risk_data)
    
    if response.status_code == 200:
        result = response.json()
        print(f"  Risk Score: {result['risk_score']:.4f}")
        print(f"  Risk Level: {result['risk_level']}")
        print(f"  Recommendation: {result['recommendation']}")
        return True
    else:
        print(f"Error: {response.text}")
        return False


def test_invalid_input():
    """Test with invalid input to verify validation"""
    print("\n=== Testing Input Validation ===")
    
    invalid_data = {
        "Age": 150,  # Invalid age
        "Number_of_sexual_partners": -5,  # Negative value
    }
    
    response = requests.post(f"{API_URL}/predict", json=invalid_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:200]}...")  # Print first 200 chars
    return response.status_code == 422  # Validation error expected


if __name__ == "__main__":
    print("=" * 60)
    print("Cervical Cancer Risk Prediction API - Test Suite")
    print("=" * 60)
    print("\nMake sure the API server is running:")
    print("  cd api-endpoints")
    print("  uvicorn main:app --reload")
    print("=" * 60)
    
    try:
        # Run tests
        tests = [
            ("Health Check", test_health_check),
            ("Basic Prediction", test_prediction),
            ("High-Risk Case", test_high_risk_case),
            ("Input Validation", test_invalid_input)
        ]
        
        results = []
        for test_name, test_func in tests:
            try:
                passed = test_func()
                results.append((test_name, passed))
            except Exception as e:
                print(f"\n❌ {test_name} failed with error: {str(e)}")
                results.append((test_name, False))
        
        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        for test_name, passed in results:
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"{status}: {test_name}")
        
        total = len(results)
        passed_count = sum(1 for _, p in results if p)
        print(f"\nTotal: {passed_count}/{total} tests passed")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to API server.")
        print("Please make sure the server is running at http://localhost:8000")
