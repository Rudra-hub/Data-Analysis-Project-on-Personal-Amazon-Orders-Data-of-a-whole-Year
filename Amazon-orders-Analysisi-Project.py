#!/usr/bin/env python
# coding: utf-8
#EXECUTE THESE CODES IN JUPYTER NOTEBOOK
# # Amazon-orders Project

# AIM:
# 1.How much I spent on Amazon during this period.
# 2.What my highest, lowest, and average order totals were.
# 3.How much tax I paid, and the effective sales tax rate I paid.
# 4.How my spending fluctuated over time.
# 5.On which days I spent the most money.
# BY: RUDRA PRATAP PADHI

# In[1]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv(r'C:\Users\Rudra Pratap\Desktop\CSV\amazon-orders.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df = df.fillna(0)
df.head()


# In[6]:


df["Total Charged in Rupees"] = df["Total Charged in Rupees"].astype(float)
df.head()


# In[7]:


df["Total Charged in Rupees"].sum()


# In[8]:


df["Total Charged in Rupees"].mean()


# In[9]:


df["Total Charged in Rupees"].median()


# In[10]:


df["Total Charged in Rupees"].max()


# In[11]:


df["Total Charged in Rupees"].min()


# In[12]:


df["Tax Charged in Rupees"].sum()


# In[13]:


df["Tax Charged in Rupees"].sum() / df["Total Charged in Rupees"].sum()


# In[14]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()


# In[15]:


df.plot.bar(x='Order Date',y='Total Charged in Rupees',rot=90,figsize=(20,10),color='#99ff66')


# In[16]:


daily_orders = df.groupby('Order Date').sum()["Total Charged in Rupees"]
daily_orders.head(56)


# In[17]:


daily_orders.plot.bar(figsize=(20, 10), color='#ff99ff')

