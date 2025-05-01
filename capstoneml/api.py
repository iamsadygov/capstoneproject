from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

# Load the ranked laptop data
df = pd.read_csv("capstoneml/data/laptop_dataset.csv")

app = Flask(__name__)
CORS(app)

def expand_ranks(target_rank):
    if target_rank == 5:
        return [4, 5]
    elif target_rank == 4:
        return [3, 4, 5]
    elif target_rank == 3:
        return [2, 3, 4]
    elif target_rank == 2:
        return [1, 2, 3]
    elif target_rank == 1:
        return [1, 2]
    return [target_rank]

def filter_laptops(weights, use_expansion=False):
    filtered = df.copy()
    for aspect, weight in weights.items():
        if weight == 0:
            continue
        rank_col = f"{aspect} Rank"
        if rank_col not in filtered.columns:
            continue
        valid_ranks = expand_ranks(weight) if use_expansion else [weight]
        filtered = filtered[filtered[rank_col].isin(valid_ranks)]
    return filtered

def partial_match_score(row, weights):
    score = 0
    for aspect, desired_rank in weights.items():
        if desired_rank == 0:
            continue
        rank_col = f"{aspect} Rank"
        if rank_col not in row:
            continue
        actual_rank = row[rank_col]
        score += max(0, 5 - abs(desired_rank - actual_rank))  # 5 points for perfect match, less for close ones
    return score

@app.route("/recommend", methods=["POST"])
def recommend():
    weights = request.get_json()  # Accept direct JSON

    if not weights:
        return jsonify({"error": "Missing aspect weights"}), 400

    # First try strict filtering
    filtered_df = filter_laptops(weights, use_expansion=False)

    # If no results, apply relaxed filtering
    if filtered_df.empty:
        filtered_df = filter_laptops(weights, use_expansion=True)

    # If still no results, do partial match scoring
    if filtered_df.empty:
        scored_df = df.copy()
        scored_df["Score"] = scored_df.apply(lambda row: partial_match_score(row, weights), axis=1)
        scored_df = scored_df.sort_values(by="Score", ascending=False)
        filtered_df = scored_df

    result = filtered_df.head(10).to_dict(orient="records")
    return jsonify({ "results": result })


if __name__ == "__main__":
    app.run(debug=True, port=5000)