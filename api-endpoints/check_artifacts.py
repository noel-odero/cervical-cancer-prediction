"""Utility script to verify saved model artifacts.
Run locally with: python check_artifacts.py
"""
from pathlib import Path
import joblib


def main():
    models_dir = Path(__file__).parent.parent / "model-training" / "models"
    if not models_dir.exists():
        print(f"Models directory not found: {models_dir}")
        return

    required = ["best_model.pkl", "preprocessor.pkl", "feature_list.pkl"]
    missing = [f for f in required if not (models_dir / f).exists()]
    if missing:
        print("Missing artifact files:", ", ".join(missing))
        return

    model = joblib.load(models_dir / "best_model.pkl")
    preprocessor = joblib.load(models_dir / "preprocessor.pkl")
    feature_list = joblib.load(models_dir / "feature_list.pkl")

    print("Model class:", type(model).__name__)
    print("Feature count:", len(feature_list))
    print("Features (ordered):")
    for i, f in enumerate(feature_list, 1):
        print(f"  {i}. {f}")

    # Simple shape check for transformer
    try:
        if hasattr(preprocessor, 'transform'):
            print("Preprocessor loaded successfully (has transform method).")
    except Exception as e:
        print("Preprocessor check failed:", e)

    expected_features = [
        'Number of sexual partners',
        'First sexual intercourse',
        'Smokes',
        'Hormonal Contraceptives',
        'IUD (years)',
        'STDs',
        'STDs (number)',
        'STDs:cervical condylomatosis',
        'STDs:pelvic inflammatory disease',
        'STDs:genital herpes'
    ]

    if feature_list == expected_features:
        print("Feature list matches expected 10 VIF-selected features.")
    else:
        print("WARNING: Feature list does not match expected set.")
        missing_expected = [f for f in expected_features if f not in feature_list]
        extra = [f for f in feature_list if f not in expected_features]
        if missing_expected:
            print("  Missing expected:", missing_expected)
        if extra:
            print("  Unexpected extras:", extra)


if __name__ == "__main__":
    main()
