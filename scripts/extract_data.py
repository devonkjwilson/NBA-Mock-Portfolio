import pandas as pd

# Define file path
Players_path = "data/Players.csv"  # Update the path if needed
LeaugeSchedule_path = "data/LeagueSchedule24_25.csv"
Playerstats_path = "data/PlayerStatistics (1).xlsx"
TeamHistories_path = "data/TeamHistories.csv"
TeamStats_path = "data/TeamStatistics.csv"
try:
    # Load CSV file
    df = pd.read_csv(Players_path)
    print(f"✅ Successfully extracted data from {Players_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {Players_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")
try:
    # Load CSV file
    df = pd.read_csv(LeaugeSchedule_path)
    print(f"✅ Successfully extracted data from {LeaugeSchedule_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {LeaugeSchedule_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")

try:
    # Load CSV file
    df = pd.read_csv(Playerstats_path)
    print(f"✅ Successfully extracted data from {Playerstats_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {Playerstats_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")

try:
    # Load CSV file
    df = pd.read_csv(TeamHistories_path)
    print(f"✅ Successfully extracted data from {TeamHistories_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {TeamHistories_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")

try:
    # Load CSV file
    df = pd.read_csv(TeamStats_path)
    print(f"✅ Successfully extracted data from {TeamStats_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {TeamStats_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")
