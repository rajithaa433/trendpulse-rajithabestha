#!/usr/bin/env python
# coding: utf-8

# Task 2 — Data Processing (task2_data_processing.py)

# In[1]:


import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Remove 'isPartial' column if exists
if 'isPartial' in df.columns:
    df = df.drop(columns=['isPartial'])

# Handle missing values
df = df.fillna(method='ffill')

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved to cleaned_data.csv")


# In[ ]:




