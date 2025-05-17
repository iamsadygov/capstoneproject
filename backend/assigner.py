import pandas as pd
import joblib
import numpy as np

aspects = {
    'cpu': 'CPU',
    'gpu': 'Graphic Card',
    'ram': 'RAM',
    'weight': 'Weight',
    'color': 'Color',
    'brand': 'Brand',
    'os': 'Operating System',
    'memory_speed': 'Memory Speed',
    'screen_size': 'Screen Size',
    'storage': 'Storage'
}


df = pd.read_csv("data/aspect_data.csv")

def convert_to_rank(preds):
    preds_noisy = preds + np.random.normal(0, 0.001, size=len(preds))  
    return pd.cut(preds_noisy, bins=5, labels=[1, 2, 3, 4, 5]).astype(int)

for key, col in aspects.items():
    print(f"▶ Ranking aspect: {col}")

    model = joblib.load(f"model/{key}_rank.pkl")

    with open(f"model/{key}_encoder_columns.txt") as f:
        expected_columns = [line.strip() for line in f.readlines()]

    encoded = pd.get_dummies(df[[col]].astype(str))

    for missing in set(expected_columns) - set(encoded.columns):
        encoded[missing] = 0

    encoded = encoded[expected_columns]

    preds = model.predict(encoded)

    df[f"{col} Rank"] = convert_to_rank(preds)

df.to_csv("data/laptop_data.csv", index=False)
print("==\laptop_data is ready for use/==")
