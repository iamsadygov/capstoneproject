import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

brand_sales = pd.read_csv('data/brand_sales.csv')

X = brand_sales[['Brand']]
y = brand_sales['SalesPreference']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/brand_rank.pkl')

with open('model/brand_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
