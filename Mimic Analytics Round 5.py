#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


cluster1 = pd.read_csv("/Users/fez/Downloads/cluster-analysis-1.csv")
cluster3 = pd.read_csv("/Users/fez/Downloads/cluster-analysis-3.csv")
cluster3
cluster2 = pd.read_csv("/Users/fez/Downloads/cluster-analysis-2.csv")


# In[5]:


cluster3.groupby("Cluster").mean("Number of Items Purchased from Buhi")


# In[7]:


cluster2


# In[ ]:





# In[8]:


cluster2.groupby("Cluster").mean("Number of Items Purchased from Buhi")


# In[9]:


cluster2.groupby("Cluster").sum("Number of Items Purchased from Buhi")


# In[ ]:




