import pandas as pd

ranked_df = pd.read_csv('./data/ranked_aspect_data.csv')

verified_df = pd.read_csv('./data/verification_data.csv')

aspect_data = pd.read_csv('./data/aspect_data.csv')

aspects = [
    'CPU', 'Graphic Card', 'RAM', 'Storage', 'Memory Speed',
    'Screen Size', 'Weight', 'Brand', 'Operating System', 'Color'
]

for aspect in aspects:
    aspect_data[f'{aspect} Rank'] = ranked_df[f'{aspect} Rank']

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

aspect_data['Correctness Score (%)'] = similarity_scores

aspect_data.to_csv('./data/laptop_dataset.csv', index=False)
print("laptop_dataset.csv generated successfully with ranks and correctness scores.")