import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load storage sales data
storage_sales = pd.read_csv('data/storage_sales.csv')

# Feature and target
X = storage_sales[['Storage']]
y = storage_sales['SalesPreference']

# One-hot encoding (for consistency, even if numeric)
X_encoded = pd.get_dummies(X.astype(str))

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/storage_rank.pkl')

# Save encoder columns
with open('model/storage_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")