#!/usr/bin/env python
# coding: utf-8

# # Data Analysis Project

# ## Importing Libraries (Toolkit)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Importing & Inspecting Data

# In[8]:


data = pd.read_excel('startup-expansion.xlsx')
data


# In[3]:


data.info()


# In[7]:


data[['Marketing Spend','Revenue']].describe().round(2)


# ## Data Preprocessing

# In[20]:


print(data['City'].unique())
print(data['City'].nunique())
print(data['City'].value_counts())


# In[21]:


print(data['State'].unique())
print(data['State'].nunique())
print(data['State'].value_counts())


# In[22]:


print(data['Sales Region'].unique())
print(data['Sales Region'].nunique())
print(data['Sales Region'].value_counts())


# In[24]:


print(data['New Expansion'].unique())
print(data['New Expansion'].nunique())
print(data['New Expansion'].value_counts())


# In[26]:


print(data.isna().sum())
print(data.duplicated().sum())


# ## Data Analysis

# In[32]:


data[data['New Expansion'] == 'Old'].groupby(['State']).sum()['Revenue'].nlargest(10)


# In[31]:


data[data['New Expansion'] == 'New'].groupby(['State']).sum()['Revenue'].nlargest(10)


# In[39]:


data['Sales Region'].value_counts().plot.bar()


# In[41]:


data['Profit'] = data['Revenue'] - data['Marketing Spend']


# In[46]:


data['ROMS'] = round((data['Profit'] / data['Marketing Spend'] * 100),2)
data['ROMS%'] = round((data['Profit'] / data['Marketing Spend'] * 100),2)/100


# In[48]:


data.to_csv('startup-expansion-modified.csv')


# In[ ]:




