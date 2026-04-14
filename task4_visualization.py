#!/usr/bin/env python
# coding: utf-8

# Task 4 — Visualization (task4_visualization.py)

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cleaned_data.csv")

# Plot trends
df.plot(figsize=(10, 6))
plt.title("Trending Topics Over Time")
plt.xlabel("Index")
plt.ylabel("Trend Score")
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




