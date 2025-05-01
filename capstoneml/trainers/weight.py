import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

weight_sales = pd.read_csv('data/weight_sales.csv')

X = weight_sales[['Weight']]
y = weight_sales['SalesPreference']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/weight_rank.pkl')

with open('model/weight_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
