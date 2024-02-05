#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv('clothes_price_prediction_data.csv')


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.tail()


# In[8]:


sns.countplot(x='Brand',data=data)


# In[9]:


data.Brand.value_counts()


# In[10]:


plt.figure(figsize=(20,25),facecolor='white')
plotnumber=1

for column in data:
    if plotnumber<=9:
        #ax is axis
        ax=plt.subplot(3,3,plotnumber)
        sns.histplot(data[column])
        plt.xlabel(column,fontsize=20)
        plt.ylabel('Count',fontsize=20)
    plotnumber+=1
plt.tight_layout()


# In[15]:


#hue distribute data according to data
sns.countplot(x='Size',hue='Color',data=data)
plt.show()


# In[17]:


sns.histplot(x='Brand',hue='Category',data=data)


# In[18]:


sns.relplot(x='Size',y='Color',hue='Material',data=data)
plt.show()


# In[23]:


sns.histplot(x='Size',hue='Material',data=data)


# In[25]:


sns.relplot(x='Price',y='Size',col='Material',data=data)
plt.show()


# In[26]:


data.isnull().sum()


# In[27]:


data.columns


# In[ ]:





# In[ ]:




