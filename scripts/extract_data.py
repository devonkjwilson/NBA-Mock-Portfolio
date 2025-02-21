import os
import pandas as pd

# Define file paths
file_paths = {
    "Games": "data/Games.csv",
    "League Schedule": "data/LeagueSchedule24_25.csv",
    "Players": "data/Players.csv",
    "Team Histories": "data/TeamHistories.csv",
    "Team Stats": "data/TeamStatistics.csv",
}

# Function to load CSV in chunks for large files
def load_csv(file_path, chunk_size=100000):
    try:
        # Check if file exists and is not empty
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            print(f"❌ Error: {file_path} is missing or empty.")
            return None
        
        # Read large files in chunks
        chunk_list = []
        for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
            chunk_list.append(chunk)
        df = pd.concat(chunk_list, ignore_index=True)
        
        print(f"✅ Successfully loaded {file_path} ({len(df)} rows)")
        print(df.head())  # Show first 5 rows
        return df

    except pd.errors.EmptyDataError:
        print(f"❌ Error: {file_path} has no columns to parse.")
    except Exception as e:
        print(f"❌ Unexpected Error loading {file_path}: {e}")
    return None

# Dictionary to store loaded DataFrames
dataframes = {}

# Load each file
for name, path in file_paths.items():
    dataframes[name] = load_csv(path)

# Handle Excel file separately
try:
    player_stats_path = "data/PlayerStatistics (1).xlsx"
    if os.path.exists(player_stats_path) and os.path.getsize(player_stats_path) > 0:
        player_stats_df = pd.read_excel(player_stats_path, engine="openpyxl")
        print(f"✅ Successfully loaded {player_stats_path} ({len(player_stats_df)} rows)")
        print(player_stats_df.head())  # Show first 5 rows
        dataframes["Player Stats"] = player_stats_df
    else:
        print(f"❌ Error: {player_stats_path} is missing or empty.")
except Exception as e:
    print(f"❌ Unexpected Error loading {player_stats_path}: {e}")

# ✅ Now, all DataFrames are stored in `dataframes` dictionary
