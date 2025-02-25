import os
import pandas as pd

# Define file paths 
file_paths = {
    "League Schedule": "data/LeagueSchedule24_25.csv",
    "Players": "data/Players.csv",
    "Team Histories": "data/TeamHistories.csv",
    "Team Statistics": "data/TeamStatistics.cvs",
    "Player Statistics": "data/PlayerStatistics (1).xlsx",
    "Games": "data/Games.csv"
}

# Function to load CSV files efficiently
def load_csv(file_path, chunk_size=100000):
    try:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} is missing.")
            return None
        
        # Read large files in chunks
        df_list = []
        for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
            df_list.append(chunk)
        df = pd.concat(df_list, ignore_index=True)

        print(f"✅ Successfully loaded {file_path} ({len(df)} rows)")
        return df

    except pd.errors.EmptyDataError:
        print(f"❌ Error: {file_path} has no columns to parse.")
    except Exception as e:
        print(f"❌ Unexpected Error loading {file_path}: {e}")
    return None

# Function to load Excel files correctly
def load_excel(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"❌ Error: {file_path} is missing.")
            return None
        
        df = pd.read_excel(file_path, engine="openpyxl")
        print(f"✅ Successfully loaded {file_path} ({len(df)} rows)")
        return df

    except Exception as e:
        print(f"❌ Unexpected Error loading {file_path}: {e}")
    return None

# Dictionary to store loaded DataFrames
dataframes = {}

# Load CSV and Excel files
for name, path in file_paths.items():
    if path.endswith(".csv"):
        dataframes[name] = load_csv(path)
    elif path.endswith(".xlsx"):
        dataframes[name] = load_excel(path)

# Show the first few rows of each dataset for verification
for name, df in dataframes.items():
    if df is not None:
        print(f"\n🔍 Preview of {name}:")
        print(df.head())

# 📌 Merge Players with Player Statistics
player_merged_df = pd.merge(player_stats_df, players_df, on="personId", how="left")

# 📌 Merge Games with Team Statistics
team_merged_df = pd.merge(games_df, team_stats_df, on="gameId", how="left")

# 📌 Merge Team Histories
final_team_df = pd.merge(team_merged_df, team_histories_df, on="teamId", how="left")

# 📌 Merge Team Data with Player Data
final_df = pd.merge(final_team_df, player_merged_df, on="gameId", how="left")

# 📌 Save final merged dataset
output_path = "data/final_merged_dataset.csv"
final_df.to_csv(output_path, index=False)

print(f"✅ Successfully merged datasets and saved as {output_path}")
print(final_df.head())  # Preview first 5 rows
