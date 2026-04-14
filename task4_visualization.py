# task4_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load Data
# -------------------------------

file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)

print(f"Loaded {len(df)} cleaned stories\n")

# -------------------------------
# Step 2: Category Distribution
# -------------------------------

category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# Step 3: Top 5 Stories by Score
# -------------------------------

top_stories = df.sort_values(by="score", ascending=False).head(5)

plt.figure()
plt.barh(top_stories["title"], top_stories["score"])
plt.title("Top 5 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Title")
plt.tight_layout()
plt.show()

# -------------------------------
# Step 4: Score Distribution
# -------------------------------

plt.figure()
plt.hist(df["score"], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# -------------------------------
# Step 5: Score vs Comments
# -------------------------------

plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.show()

# -------------------------------
# Step 6: Avg Score per Category
# -------------------------------

avg_scores = df.groupby("category")["score"].mean()

plt.figure()
avg_scores.plot(kind="bar")
plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
