##         ███████╗ █████╗ ██████╗ ██╗   ██╗ ██████╗  ██████╗ ██╗   ██╗
##         ██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔═══██╗██║   ██║
##         ███████╗███████║██║  ██║ ╚████╔╝ ██║  ███╗██║   ██║██║   ██║
##         ╚════██║██╔══██║██║  ██║  ╚██╔╝  ██║   ██║██║   ██║╚██╗ ██╔╝
##         ███████║██║  ██║██████╔╝   ██║   ╚██████╔╝╚██████╔╝ ╚████╔╝
##         ╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝    ╚═════╝  ╚═════╝   ╚═══╝


from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import json
import os

DATA_PATH = "data/laptop_dataset.csv"
EDAS_PATH = "data/edas_data.csv"
SEEN_FILE = "shown_laptops.json"
USE_PERSISTENT_STORAGE = False

app = Flask(__name__)
CORS(app)

df = pd.read_csv(DATA_PATH)
edas_df = pd.read_csv(EDAS_PATH)

def load_seen():
    if USE_PERSISTENT_STORAGE and os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    if USE_PERSISTENT_STORAGE:
        with open(SEEN_FILE, "w", encoding="utf-8") as f:
            json.dump(list(seen), f, ensure_ascii=False)

shown_laptops = load_seen()

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
        score += max(0, 5 - abs(desired_rank - actual_rank))
    return score

@app.route("/recommend", methods=["POST"])
def recommend():
    global shown_laptops

    weights = request.get_json()
    if not weights:
        return jsonify({"error": "Missing aspect weights"}), 400

    # --- ML Logic ---
    filtered_df = filter_laptops(weights, use_expansion=False)
    if filtered_df.empty:
        filtered_df = filter_laptops(weights, use_expansion=True)
    if filtered_df.empty:
        scored_df = df.copy()
        scored_df["Score"] = scored_df.apply(lambda row: partial_match_score(row, weights), axis=1)
        filtered_df = scored_df.sort_values(by="Score", ascending=False)

    filtered_df = filtered_df[~filtered_df["Laptop Name"].isin(shown_laptops)]
    ml_result_df = filtered_df.head(5)

    # --- EDAS Logic ---
    edas_components = []
    mapping = {
        "Weight": "Weight",
        "RAM": "Ram",
        "Screen_Size": "Screen",
        "Memory_Speed": "Memory",
        "Price": "Price",
        "Storage": "Storage",
        "Graphics_Card": "Gpu",
        "CPU": "Cpu"
    }

    for key, edas_name in mapping.items():
        value = weights.get(key, 0)
        if value != 0:
            edas_components.append(f"{edas_name}{value}")

    preference_key = " ".join(edas_components)

    edas_result_df = pd.DataFrame()
    if preference_key in edas_df.columns:
        edas_subset = edas_df[["Laptop Name", preference_key]].copy()
        edas_subset = edas_subset.rename(columns={preference_key: "EDAS Score"})
        edas_subset = edas_subset.sort_values(by="EDAS Score", ascending=True).head(5)

        edas_result_df = df[df["Laptop Name"].isin(edas_subset["Laptop Name"])]
        edas_result_df = edas_result_df.merge(edas_subset, on="Laptop Name", how="left")
    else:
        print(f"[EDAS] No matching column for: {preference_key} — skipping EDAS results.")

    # Track shown laptops
    shown_laptops.update(ml_result_df["Laptop Name"].tolist())
    save_seen(shown_laptops)

    return jsonify({
        "ml": ml_result_df.to_dict(orient="records"),
        "edas": edas_result_df.to_dict(orient="records")
    })

@app.route("/reset_seen", methods=["POST"])
def reset_seen():
    global shown_laptops
    shown_laptops = set()
    save_seen(shown_laptops)
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=False, port=5000)