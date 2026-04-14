#!/usr/bin/env python
# coding: utf-8

# Task 1 — Data Collection (task1_data_collection.py)

# Fetch trending data (example: Google Trends using pytrends)

# In[8]:


get_ipython().system('pip install pytrends')


# In[9]:


from pytrends.request import TrendReq
import pandas as pd

# Initialize
pytrends = TrendReq()

# Keywords
keywords = ["AI", "Data Science", "Python", "Machine Learning"]

# Fetch data
pytrends.build_payload(keywords, timeframe='now 7-d')
data = pytrends.interest_over_time()

# Save to CSV
data.to_csv("data.csv")

print("Data collected and saved to data.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




