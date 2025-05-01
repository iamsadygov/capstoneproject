import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load weight sales data
weight_sales = pd.read_csv('data/weight_sales.csv')

# Feature and target
X = weight_sales[['Weight']]
y = weight_sales['SalesPreference']

# One-hot encoding (if weights are discrete, this is helpful)
X_encoded = pd.get_dummies(X.astype(str))

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/weight_rank.pkl')

# Save encoder columns
with open('model/weight_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
