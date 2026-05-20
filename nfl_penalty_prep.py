import pandas as pd
import os

# ── STEP 1: Point to your folder of raw CSV files ──────────────────────────
raw_folder = r"C:\Users\bryce\Desktop\Data Projects\2 - NFL Penalties\CSV Files\nflverse raw files"

# ── STEP 2: Only keep the columns we actually need ──────────────────────────
columns_to_keep = [
    "season",
    "week",
    "game_id",
    "home_team",
    "away_team",
    "penalty",
    "penalty_team",
    "penalty_type",
    "penalty_yards",
    "qtr",
    "game_seconds_remaining",
    "score_differential",
    "wp",
    "posteam_score",
    "defteam_score"
]

# ── STEP 3: Loop through every CSV file in the folder ──────────────────────
all_seasons = []

for filename in os.listdir(raw_folder):
    if filename.endswith(".csv"):
        print(f"Processing {filename}...")
        filepath = os.path.join(raw_folder, filename)

        # Load only the columns we need
        df = pd.read_csv(filepath, usecols=columns_to_keep, low_memory=False)

        # Keep only plays where a penalty actually occurred
        df = df[df["penalty"] == 1]
        
        # Keep only plays where a penalty actually occurred
        df = df[df["penalty"] == 1]

        # Fix franchise relocations
        df["penalty_team"] = df["penalty_team"].replace({"OAK": "LV", "SD": "LAC"})
        
        all_seasons.append(df)

# ── STEP 4: Stack all seasons into one combined dataframe ───────────────────
combined = pd.concat(all_seasons, ignore_index=True)

print(f"\nDone! Total penalty plays across all seasons: {len(combined)}")

# ── STEP 5: Save the combined file ──────────────────────────────────────────
output_path = r"C:\Users\bryce\Desktop\Data Projects\2 - NFL Penalties\CSV Files\nfl_penalties_combined.csv"
combined.to_csv(output_path, index=False)

print(f"File saved to: {output_path}")
