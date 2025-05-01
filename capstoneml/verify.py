import pandas as pd

# Load ranked_aspect_data (system-assigned ranks from ML trainers)
ranked_df = pd.read_csv('./data/ranked_aspect_data.csv')

# Load verification_data (real-world verified ranks)
verified_df = pd.read_csv('./data/verification_data.csv')

# Load aspect_data to merge into final dataset
aspect_data = pd.read_csv('./data/aspect_data.csv')

# Define which columns to compare (rank columns)
aspects = [
    'CPU', 'Graphic Card', 'RAM', 'Storage', 'Memory Speed',
    'Screen Size', 'Weight', 'Brand', 'Operating System', 'Color'
]

# Add rank columns from ranked_df into aspect_data
for aspect in aspects:
    aspect_data[f'{aspect} Rank'] = ranked_df[f'{aspect} Rank']

# Build a similarity score by comparing ranked vs verified ranks
similarity_scores = []

for i in range(len(ranked_df)):
    correct = 0
    total = 0
    for aspect in aspects:
        system_rank = ranked_df.loc[i, f'{aspect} Rank']
        real_rank = verified_df.loc[i, f'{aspect} Rank']
        if abs(system_rank - real_rank) <= 1:
            correct += 1
        total += 1
    similarity = round((correct / total) * 100, 2)
    similarity_scores.append(similarity)

# Attach correctness score
aspect_data['Correctness Score (%)'] = similarity_scores

# Save final dataset
aspect_data.to_csv('./data/laptop_dataset.csv', index=False)
print("laptop_dataset.csv generated successfully with ranks and correctness scores.")