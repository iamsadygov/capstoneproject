import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load OS sales data
os_sales = pd.read_csv('data/os_sales.csv')

# Feature and target
X = os_sales[['os']]
y = os_sales['SalesPreference']

# One-hot encoding
X_encoded = pd.get_dummies(X)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/os_rank.pkl')

# Save encoder columns
with open('model/os_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
