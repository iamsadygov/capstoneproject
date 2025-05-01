import pandas as pd

# Load the ranked data
df = pd.read_csv("data/ranked_aspect_data.csv")

# List all rank columns
rank_columns = [col for col in df.columns if "Rank" in col]

# Print unique values per rank column
for col in rank_columns:
    unique_ranks = sorted(df[col].dropna().unique())
    print(f"{col}: {unique_ranks}")
