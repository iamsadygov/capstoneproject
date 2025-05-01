import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load screen size sales data
screen_sales = pd.read_csv('data/screen_sales.csv')

# Feature and target
X = screen_sales[['ScreenSize']]
y = screen_sales['SalesPreference']

# One-hot encoding (for consistent structure, even if numeric)
X_encoded = pd.get_dummies(X.astype(str))

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/screen_size_rank.pkl')

# Save encoder columns
with open('model/screen_size_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
