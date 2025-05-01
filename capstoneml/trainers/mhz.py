import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load MHz sales data
mhz_sales = pd.read_csv('data/mhz_sales.csv')

# Feature and target
X = mhz_sales[['mhz']]
y = mhz_sales['SalesPreference']

# One-hot encoding (not needed if MHz is numeric, but kept for consistency)
X_encoded = pd.get_dummies(X.astype(str))  # cast to string to allow encoding

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/memory_speed_rank.pkl')

# Save encoder columns
with open('model/memory_speed_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
