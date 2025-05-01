import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

os_sales = pd.read_csv('data/os_sales.csv')

X = os_sales[['os']]
y = os_sales['SalesPreference']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/os_rank.pkl')

with open('model/os_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
