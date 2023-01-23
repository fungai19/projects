#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statsmodels.api as sm
import numpy as np
import seaborn as sns
#Worked with Azza, Austin and Isaac.


# In[2]:


mydata =  pd.read_excel("/Users/fez/Downloads/redbull.xlsx")


# In[3]:


#1
x = mydata['ezine']
y = mydata['sales']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit() 
print(model.summary())


# In[4]:


#predicted sales amount for spending $100

z= [1, 100]

print('predicted sales amount =', model.predict(z))


# In[5]:


#6
dummies = pd.get_dummies(mydata["region"])
mydata = mydata.join(dummies)
mydata


# In[6]:


sns.regplot(mydata.ezine, mydata.sales, ci=None)


# In[7]:


#2
Logsales = np.log(mydata['sales'])
Logsales


# In[8]:


x = mydata['ezine']
y = Logsales
x = sm.add_constant(x)
model = sm.OLS(y, x).fit() 
print(model.summary())


# In[9]:


sns.regplot(mydata.ezine, Logsales, ci=None)


# In[10]:


#3
x = mydata[['facebook', 'twitter', 'banner', 'instagram', 'youtube', 'tv','ezine']]
y = mydata['sales']
x = sm.add_constant(x) # adds a column of ones to the design matrix
model = sm.OLS(y, x).fit() # fit the regression line
print(model.summary()) # display regression results 


# In[11]:


#5
#1. Does it improve adjusted R2?
        #Removing each variable other than instagram or ezine improves adjusted R2.
#2. Does it have an insignificant p-value?
        # Each removed variable had an insignificant p-value
#3. Is it associated with response by itself?
        # None of the removed variables were strongly associated with the response variable
#4. Is it strongly associated with another explanatory variables? (If yes, then including
#       both may be redundant.)
        # Ezine and Instagram are not strongly associated with each other so including both is not an issue
#5. Does common sense say it should contribute to the model?
        # Common sense would say that any of these variables could or could not be included, so I will include the variables that make the most statistical sense
#6. What would you eliminate from the model?
        # I eliminated all variables except instagram and ezine because they had high p-values and decreased the adjusted R2 


# In[12]:


#7
x = mydata[['facebook', 'twitter', 'banner', 'instagram', 'youtube', 'tv', 'ezine', 'S']]
y = mydata['sales']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit() # fit the regression line
print(model.summary()) # display regression results 


# In[13]:


#8
mydata['interaction'] = mydata['ezine']*mydata['S']
x = mydata['interaction']
y = mydata['sales']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())


# In[14]:


#8a
# C. Ezine’s association with sales depends on the region but it is not yet clear how
        # This statement is true, as the adjusted R2 of the model changes when we change what regions the interaction
            # term includes, but this relationship in unclear still. The relationship appears to be stronger for the West.


# In[15]:


mydata['nonWest'] = mydata.N + mydata.S + mydata.E


# In[16]:


mydata['interactionWest'] = mydata['ezine']*mydata['W']
mydata['interactionNonWest'] = mydata['ezine']*mydata['nonWest']
x = mydata['interactionNonWest']
y = mydata['sales']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())


# In[17]:


#10
mydata['interactionWest'] = mydata['twitter']*mydata['W']
mydata['interactionNonWest'] = mydata['twitter']*mydata['nonWest']
x = mydata['interactionNonWest']
y = mydata['sales']
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())


# In[18]:


mydataW = mydata[mydata.W == 1]
mydataNW = mydata[mydata.nonWest == 1]
sns.regplot(mydataW.twitter, mydataW.sales, ci=None)


# In[19]:


sns.regplot(mydataNW.twitter, mydataNW.sales, ci=None)


# In[ ]:


# We changed one extreme twitter outlier that was 78,000 or something to 0 because it made no sense and was heavily skewing the graph to make it impossible to read.
# A. 
    # There is a clear difference for the West plot showing that as tweets increased, redbull sales in the West decreased.

