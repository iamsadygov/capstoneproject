import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load Brand sales data
brand_sales = pd.read_csv('data/brand_sales.csv')

# Feature and target
X = brand_sales[['Brand']]
y = brand_sales['SalesPreference']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/brand_rank.pkl')

# Save encoder columns
with open('model/brand_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
