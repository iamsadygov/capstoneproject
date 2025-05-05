import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

screen_sales = pd.read_csv('data/screen_sales.csv')

X = screen_sales[['Value']]
y = screen_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/screen_size_rank.pkl')

with open('model/screen_size_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
