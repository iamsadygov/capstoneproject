import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

gpu_sales = pd.read_csv('data/gpu_sales.csv')

X = gpu_sales[['Value']]
y = gpu_sales['Sales']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/gpu_rank.pkl')

with open('model/gpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")