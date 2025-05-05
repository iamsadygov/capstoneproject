import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

mhz_sales = pd.read_csv('data/mhz_sales.csv')

X = mhz_sales[['Value']]
y = mhz_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str)) 

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/memory_speed_rank.pkl')

with open('model/memory_speed_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
