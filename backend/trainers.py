import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

cpu_sales = pd.read_csv('salesdata/cpu_sales.csv')

X = cpu_sales[['Value']]
y = cpu_sales['Sales']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/cpu_rank.pkl')

with open('model/cpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
gpu_sales = pd.read_csv('salesdata/gpu_sales.csv')

X = gpu_sales[['Value']]
y = gpu_sales['Sales']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/gpu_rank.pkl')

with open('model/gpu_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
color_sales = pd.read_csv(
    'salesdata/color_sales.csv',
    encoding='utf-8-sig',
    quotechar='"',
    skipinitialspace=True
)

color_sales.columns = [col.strip().lower() for col in color_sales.columns]

X = pd.get_dummies(color_sales[['value']].astype(str))
y = color_sales['sales']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'model/color_rank.pkl')
with open('model/color_encoder_columns.txt', 'w') as f:
    for col in X.columns:
        f.write(f"{col}\n")
        
brand_sales = pd.read_csv('salesdata/brand_sales.csv')

X = brand_sales[['Value']]
y = brand_sales['Sales']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/brand_rank.pkl')

with open('model/brand_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")

mhz_sales = pd.read_csv('salesdata/mhz_sales.csv')

X = mhz_sales[['Value']]
y = mhz_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str)) 

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/memory_speed_rank.pkl')

with open('model/memory_speed_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")

os_sales = pd.read_csv('salesdata/os_sales.csv')

X = os_sales[['Value']]
y = os_sales['Sales']

X_encoded = pd.get_dummies(X)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/os_rank.pkl')

with open('model/os_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
ram_sales = pd.read_csv('salesdata/ram_sales.csv')

X = ram_sales[['Value']]
y = ram_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/ram_rank.pkl')

with open('model/ram_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
screen_sales = pd.read_csv('salesdata/screen_sales.csv')

X = screen_sales[['Value']]
y = screen_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/screen_size_rank.pkl')

with open('model/screen_size_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
storage_sales = pd.read_csv('salesdata/storage_sales.csv')

X = storage_sales[['Value']]
y = storage_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/storage_rank.pkl')

with open('model/storage_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")
        
weight_sales = pd.read_csv('salesdata/weight_sales.csv')

X = weight_sales[['Value']]
y = weight_sales['Sales']

X_encoded = pd.get_dummies(X.astype(str))

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

joblib.dump(model, 'model/weight_rank.pkl')

with open('model/weight_encoder_columns.txt', 'w') as f:
    for col in X_encoded.columns:
        f.write(f"{col}\n")