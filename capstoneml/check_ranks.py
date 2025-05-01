import pandas as pd

df = pd.read_csv("data/ranked_aspect_data.csv")

rank_columns = [col for col in df.columns if "Rank" in col]

for col in rank_columns:
    unique_ranks = sorted(df[col].dropna().unique())
    print(f"{col}: {unique_ranks}")
