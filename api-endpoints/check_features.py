import joblib
import sys

# Load the feature list
features = joblib.load('../model-training/models/feature_list.pkl')
print(f'Number of features: {len(features)}')
print(f'\nFeatures used in training:')
for i, f in enumerate(features, 1):
    print(f'{i}. {f}')

# Check the best model
model = joblib.load('../model-training/models/best_model.pkl')
print(f'\n\nModel type: {type(model).__name__}')
