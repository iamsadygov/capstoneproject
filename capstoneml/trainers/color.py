import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the sales data
color_sales = pd.read_csv('data/color_sales.csv')

# Normalize columns
color_sales.columns = [col.strip().lower() for col in color_sales.columns]

# Rename for clarity
X = color_sales[['color']]
y = color_sales['salespreference']

# One-hot encode
X_encoded = pd.get_dummies(X)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save model
joblib.dump(model, 'model/color_rank.pkl')

# Save encoder columns (for consistency during prediction)
with open('model/color_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
