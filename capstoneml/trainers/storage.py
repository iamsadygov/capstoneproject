import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

storage_sales = pd.read_csv('data/storage_sales.csv')

X = storage_sales[['Storage']]
y = storage_sales['SalesPreference']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/storage_rank.pkl')

with open('model/storage_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")