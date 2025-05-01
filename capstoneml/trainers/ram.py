import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load RAM sales data
ram_sales = pd.read_csv('data/ram_sales.csv')

# Feature and target
X = ram_sales[['RAM']]
y = ram_sales['SalesPreference']

# One-hot encoding (RAM is numeric, but we apply this for consistent handling)
X_encoded = pd.get_dummies(X.astype(str))

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/ram_rank.pkl')

# Save encoder columns
with open('model/ram_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
