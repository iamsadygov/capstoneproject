import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load GPU sales data
gpu_sales = pd.read_csv('data/gpu_sales.csv')

# Feature and target
X = gpu_sales[['GPU']]
y = gpu_sales['Sales_Count']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/gpu_rank.pkl')

# Save encoder columns
with open('model/gpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")