import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

cpu_sales = pd.read_csv('data/cpu_sales.csv')

X = cpu_sales[['CPU']]
y = cpu_sales['SalesPreference']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/cpu_rank.pkl')

with open('model/cpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")