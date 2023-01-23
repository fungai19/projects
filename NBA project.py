#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nba_api.stats.endpoints import shotchartdetail
import json

response = shotchartdetail.ShotChartDetail(
    team_id=0,
    player_id=0,
    season_nullable='2014-15',
    season_type_all_star='Regular Season'
)

content = json.loads(response.get_json())


# In[2]:


content


# In[7]:


import pandas as pd

# transform contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers

# write to csv file
df.to_csv('/Users/fez/Downloads/allstats.csv', index=False)


# In[ ]:




