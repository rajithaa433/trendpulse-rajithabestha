import pandas as pd
import os

# File path (update date if needed)
file_path = "data/trends_20260414.json"

# -------------------------------
# 1. LOAD JSON FILE
# -------------------------------
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# -------------------------------
# 2. CLEAN THE DATA
# -------------------------------

# Remove duplicates based on post_id
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove rows with missing critical fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-quality stories (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra whitespace in title
df["title"] = df["title"].str.strip()

# -------------------------------
# 3. SAVE AS CSV
# -------------------------------

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")
os.makedirs(r"C:\Users\rajit\Desktop\data", exist_ok=True)
output_file = r"C:\Users\rajit\Desktop\data\trends_clean.csv"
# output_file = "data/trends_clean.csv"

df.to_csv(output_file, index=False)

print(f"\nSaved {len(df)} rows to {output_file}")

# -------------------------------
# SUMMARY: STORIES PER CATEGORY
# -------------------------------
print("\nStories per category:")
print(df["category"].value_counts())
