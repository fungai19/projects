#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


buhi_LandingPageConversions = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_LandingPageConversions .csv")
buhi_LandingPageTraffic = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_LandingPageTraffic.csv")
buhi_Jan_sales = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_Sales-Jan.csv")
buhi_Feb_sales = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_Sales-Feb.csv")
buhi_Mar_sales = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_Sales-Mar 2.csv")
buhi_Ad_campaigns = pd.read_csv("/Users/fez/Desktop/DAIB/BUHI_SearchAdCampaign.csv")


# In[7]:


buhi_LandingPageConversions.dtypes


# In[9]:


buhi_LandingPageConversions['Ad Campaign Clicks']  = pd.to_numeric(buhi_LandingPageConversions['Ad Campaign Clicks'], errors='coerce' )


# In[5]:


buhi_LandingPageConversions.head()


# In[10]:


LandingPage_GroupSums = buhi_LandingPageConversions.groupby('Landing Page').sum()
LandingPage_GroupSums


# In[11]:


LandingPage_GroupSums['Conversion Rate'] = LandingPage_GroupSums['Converted Sales']/LandingPage_GroupSums['Ad Campaign Clicks']


# In[13]:


LandingPage_GroupSums['Conversion Rate'].idxmax()


# In[5]:


buhi_Mar_sales['Quantity of Item Purchased'].sum()


# In[ ]:


buhi_SearchAdCampaign['Profits'] = buhi_SearchAdCampaign['Total Revenue'] - buhi_SearchAdCampaign['Total Cost']
buhi_SearchAdCampaign.loc[buhi_SearchAdCampaign['Profits'].idmax()]
GroupByCampaign_SumValues = buhi_SearchAdCampaign.groupby('Ad Campaign Name').sum()
GroupByCampaign_SumValues['Conversion Rate'] = GroupByCampaign_SumValues['Total Conversions']/GroupByCampaign_SumValues['Total clicks']
GroupByCampaign_SumValues['Conversion Rate'].idmax()

CommonNames_Mar_Jan = buhi_Mar_sales['Name'].isin(buhi_Jan_sales['Name'])
CommonNames_Mar_Feb = buhi_Mar_sales['Name'].isin(buhi_Feb_sales['Name'])
buhi_Mar_sales[CommonNames_Mar_Jan] | CommonNames_Mar_Feb]

