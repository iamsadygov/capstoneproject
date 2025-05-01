import pandas as pd

# Load the preprocessed laptop dataset with ranks
laptop_df = pd.read_csv('capstoneml/data/laptop_dataset.csv')

# Define the rank columns we compare
rank_columns = [
    'CPU Rank', 'Graphic Card Rank', 'RAM Rank', 'Storage Rank', 'Memory Speed Rank',
    'Screen Size Rank', 'Weight Rank', 'Brand Rank', 'Operating System Rank', 'Color Rank'
]

# Initialize memory to store previously recommended laptop indices
suggested_indices = set()

# Function to calculate similarity (±1 tolerance)
def calculate_similarity(row, desired_ranks):
    matches = 0
    for col in rank_columns:
        if col in row and col in desired_ranks:
            if abs(row[col] - desired_ranks[col]) <= 1:
                matches += 1
    return round((matches / len(rank_columns)) * 100, 2)

# Main recommendation function
def recommend_laptops(desired_ranks, top_n=10):
    scored = []

    for idx, row in laptop_df.iterrows():
        if idx in suggested_indices:
            continue  # skip already suggested

        score = calculate_similarity(row, desired_ranks)
        scored.append((idx, score))

    # Sort by similarity score descending
    scored.sort(key=lambda x: x[1], reverse=True)

    # Select top N new laptops
    selected = []
    for idx, score in scored:
        if len(selected) < top_n:
            selected.append((idx, score))
            suggested_indices.add(idx)
        else:
            break

    # Return DataFrame with similarity included
    results = laptop_df.loc[[idx for idx, _ in selected]].copy()
    results['Similarity Score (%)'] = [score for _, score in selected]
    return results

# === Example usage ===
if __name__ == '__main__':
    # Simulate a user preference input
    desired = {
        'CPU Rank': 2,
        'Graphic Card Rank': 5,
        'RAM Rank': 3,
        'Storage Rank': 2,
        'Memory Speed Rank': 0,
        'Screen Size Rank': 0,
        'Weight Rank': 1,
        'Brand Rank': 5,
        'Operating System Rank': 1,
        'Color Rank': 5
    }

    result_df = recommend_laptops(desired)
    print("\nRecommended laptops (no repeats):\n")
    print(result_df[['Laptop Name', 'Brand', 'CPU', 'Graphic Card', 'RAM', 'Storage', 'Similarity Score (%)']])
    
    # ____ ____ ____ ____ ____ ____ ____ #
    #||S |||A |||D |||Y |||G |||O |||V ||#
    #||__|||__|||__|||__|||__|||__|||__||#
    #|/__\|/__\|/__\|/__\|/__\|/__\|/__\|#
    #                                    #