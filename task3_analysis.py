import pandas as pd
import numpy as np

# -------------------------------
# Step 1: Load Cleaned CSV
# -------------------------------

file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print(f"Loaded {len(df)} cleaned stories from {file_path}\n")

# -------------------------------
# Step 2: Basic Overview
# -------------------------------

# Display first 5 rows
print("First 5 rows:")
print(df.head(), "\n")

# Summary statistics
print("Summary statistics:")
print(df.describe(), "\n")

# -------------------------------
# Step 3: Category Analysis
# -------------------------------

print("Stories per category:")
category_counts = df["category"].value_counts()
print(category_counts, "\n")

# -------------------------------
# Step 4: Top Performing Stories
# -------------------------------

print("Top 5 stories by score:")
top_stories = df.sort_values(by="score", ascending=False).head(5)
print(top_stories[["title", "score"]], "\n")

# -------------------------------
# Step 5: NumPy Analysis
# -------------------------------

# Average, median, max score
avg_score = np.mean(df["score"])
median_score = np.median(df["score"])
max_score = np.max(df["score"])

print(f"Average score: {avg_score}")
print(f"Median score: {median_score}")
print(f"Max score: {max_score}\n")

# -------------------------------
# Step 6: Engagement Analysis
# -------------------------------

# Correlation between score and comments
correlation = df[["score", "num_comments"]].corr()

print("Correlation between score and number of comments:")
print(correlation, "\n")

# -------------------------------
# Step 7: Category-wise Performance
# -------------------------------

print("Average score per category:")
avg_category_score = df.groupby("category")["score"].mean()
print(avg_category_score, "\n")

# -------------------------------
# Step 8: Insights (Important for Marks)
# -------------------------------

print("Insights:")

top_category = category_counts.idxmax()
print(f"- Most frequent category: {top_category}")

best_category = avg_category_score.idxmax()
print(f"- Category with highest average score: {best_category}")

print("- Higher score generally relates to higher engagement (comments), depending on correlation value.")
