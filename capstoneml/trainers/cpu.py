import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load CPU sales data
cpu_sales = pd.read_csv('data/cpu_sales.csv')

# Feature and target
X = cpu_sales[['CPU']]
y = cpu_sales['SalesPreference']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/cpu_rank.pkl')

# Save encoder columns for prediction
with open('model/cpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")