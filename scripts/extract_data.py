import pandas as pd

# Define file path
file_path = "../data/Players.csv"  # Adjust path if needed

try:
    # Load CSV file
    df = pd.read_csv(file_path)
    print(f"✅ Successfully extracted data from {file_path}")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print(f"❌ Error: File {file_path} not found.")
except Exception as e:
    print(f"❌ Error: {e}")
