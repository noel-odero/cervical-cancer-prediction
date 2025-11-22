"""Basic structure tests for predict_cervical_cancer_risk using new 10-feature set.
Run: python test_prediction.py
"""
import sys
sys.path.insert(0, '.')

from predict import predict_cervical_cancer_risk

low_risk_example = {
    'Number of sexual partners': 2,
    'First sexual intercourse': 18,
    'Smokes': 0,
    'Hormonal Contraceptives': 1,
    'IUD (years)': 0,
    'STDs': 0,
    'STDs (number)': 0,
    'STDs:cervical condylomatosis': 0,
    'STDs:pelvic inflammatory disease': 0,
    'STDs:genital herpes': 0
}

higher_risk_example = {
    'Number of sexual partners': 25,
    'First sexual intercourse': 14,
    'Smokes': 1,
    'Hormonal Contraceptives': 1,
    'IUD (years)': 10,
    'STDs': 1,
    'STDs (number)': 6,
    'STDs:cervical condylomatosis': 1,
    'STDs:pelvic inflammatory disease': 1,
    'STDs:genital herpes': 1
}

def run_case(name, payload):
    print(f"\n[TEST] {name}")
    result = predict_cervical_cancer_risk(payload)
    print(f"Risk Score: {result['risk_score']:.4f}")
    print(f"Risk Level: {result['risk_level']}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"Model Used: {result['model_used']}")
    # Basic assertions
    assert 'risk_score' in result
    assert 'risk_level' in result
    assert 'recommendation' in result
    assert 'model_used' in result
    assert 0.0 <= result['risk_score'] <= 1.0

if __name__ == '__main__':
    print("=" * 60)
    print("Testing prediction structure with updated feature set")
    print("=" * 60)
    run_case("LOW RISK EXAMPLE", low_risk_example)
    run_case("HIGHER RISK EXAMPLE", higher_risk_example)
    print("\nAll structure tests passed.")
