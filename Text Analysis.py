#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import nltk
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


filename = '/Users/fez/Desktop/Lincoln.txt'
file = open(filename, 'rt') # open the text file
text = file.read() #read the text file

print(text)


# In[3]:


text = text.lower()
text


# In[4]:


from nltk import sent_tokenize

sentences = sent_tokenize(text)

print(sentences[0])


# In[5]:


from nltk import word_tokenize

tokens = word_tokenize(text)

print(tokens[:100])


# In[7]:


words = [word for word in tokens if word.isalpha()]

print(words[:100]) # print the first 100 words


# In[8]:


print('number of words: {0}'.format(len(words)))


# In[9]:


print('length of first word: {0}'.format(len(words[1])))


# In[10]:


tab = pd.Series(words).value_counts()


# In[11]:


tab = pd.DataFrame({'word': tab.index, 'count': tab.values})

print(tab)


# In[ ]:




