import pandas as pd

# Define file path
Players_path = "data/Players.csv"  # Update the path if needed

try:
    # Load CSV file
    df = pd.read_csv(Players_path)
    print(f"✅ Successfully extracted data from {Players_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {Players_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")
