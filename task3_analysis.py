#!/usr/bin/env python
# coding: utf-8

# Task 3 — Analysis (task3_analysis.py)

# In[1]:


import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Basic statistics
print("Summary Statistics:\n", df.describe())

# Find most trending topic
avg_trends = df.mean()
top_trend = avg_trends.idxmax()

print("\nMost trending topic:", top_trend)


# In[ ]:




