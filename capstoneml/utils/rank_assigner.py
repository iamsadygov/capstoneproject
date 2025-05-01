import pandas as pd
import joblib
import numpy as np

# Define aspect mapping: model filename key → column name in CSV
aspects = {
    'cpu': 'CPU',
    'gpu': 'Graphic Card',
    'ram': 'RAM',
    'weight': 'Weight',
    'color': 'Color',
    'brand': 'Brand',
    'os': 'Operating System',
    'mhz': 'Memory Speed',
    'screen': 'Screen Size',
    'storage': 'Storage'
}

# Load your latest aspect data
df = pd.read_csv("data/aspect_data.csv")

# Function: map model predictions into 1–5 ranks using value binning
def convert_to_rank(preds):
    preds_noisy = preds + np.random.normal(0, 0.001, size=len(preds))  # avoids bin edge ties
    return pd.cut(preds_noisy, bins=5, labels=[1, 2, 3, 4, 5]).astype(int)

# Loop through each aspect to assign rank
for key, col in aspects.items():
    print(f"▶ Ranking aspect: {col}")

    # Load regressor model
    model = joblib.load(f"model/{key}_rank.pkl")

    # Load encoder columns to match training structure
    with open(f"model/{key}_encoder_columns.txt") as f:
        expected_columns = [line.strip() for line in f.readlines()]

    # One-hot encode the actual values from aspect_data.csv
    encoded = pd.get_dummies(df[[col]].astype(str))

    # Add missing dummy columns if any are not present in the real data
    for missing in set(expected_columns) - set(encoded.columns):
        encoded[missing] = 0

    # Ensure order consistency with the training data
    encoded = encoded[expected_columns]

    # Predict rank scores using trained model
    preds = model.predict(encoded)

    # Convert model output to rank bins
    df[f"{col} Rank"] = convert_to_rank(preds)

# Save ranked version of dataset
df.to_csv("data/ranked_aspect_data.csv", index=False)
print("✅ All aspects ranked and saved to data/ranked_aspect_data.csv")
