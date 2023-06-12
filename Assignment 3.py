#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import seaborn as sns
import pandas as pd
import os


# 1st dataset -- EDA

# In[6]:


df = pd.read_csv("Airbnb Dataset 19.csv")


# In[7]:


df.sample()


# In[8]:


df.info()


# In[151]:


df.shape


# In[9]:


df.describe()


# In[10]:


df.isnull()


# Finding the correlation among different variables

# In[11]:


correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plot.title('Correlation Matrix')
plot.show()


# chceking the categorical data

# In[12]:


categorical = df.dtypes[df.dtypes == "object"].index
print(categorical)


# In[13]:


df[categorical].describe()


# In[14]:


df.describe()


# In[15]:


sorted(df["host_name"])[0:21]


# In[44]:


df["name"].describe()


# In[47]:


df


# In[48]:


df.describe()


# In[16]:


df.plot.box()


# **Graph 1 - Histogram ( to check skewness of the dataset (as per the figure it's  left-skewed distribution)) - Reason for choosing this graph is it shows what is the average price this industry and what is the minimum price that a person has to pay by a segement of people)

# In[17]:


df.hist(column = "price", figsize = (9,5), bins = 10)


# **Graph 2 - Scatter Plot (to detect outliers and to find the correlation between two variables) - In the below graph outlier is clearly depicted as it's away from the dataset and each segement has different sort price segment which people can affort)

# In[18]:


df.plot(kind = 'scatter', x = 'room_type', y = 'price')


# **Graph 3 - Scatter plot 

# In[19]:


df.plot(kind = 'scatter', x = 'neighbourhood_group', y = 'price')


# **Graph 4 - Line chart

# In[20]:


df.plot("neighbourhood_group","number_of_reviews")


# **2nd dataset -- EDA

# In[21]:


df = pd.read_csv("HRDataset_v14.csv")
df


# In[22]:


df.sample()


# In[25]:


df.info()


# In[27]:


df.shape


# In[28]:


df.isnull()


# In[29]:


correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plot.title('Correlation Matrix')
plot.show()


# In[23]:


pd.set_option("display.max.columns",None)
df.head(11)


# In[97]:


del df["Employee_Name"]


# In[98]:


del df["EmpID"]
del df["FromDiversityJobFairID"]


# In[99]:


df.describe()


# In[101]:


df.dtypes


# In[102]:


categorical = df.dtypes[df.dtypes == "object"].index
print(categorical)


# In[104]:


df[categorical].describe()


# In[116]:


nw_gen = pd.Categorical(df["Sex"])
nw_gen = nw_gen.rename_categories(["Male","Female"])



nw_gen.describe()


# **Graph 3 - Pie chart - check the ratio of the visits in this industry

# In[133]:


df["Sex"] = nw_gen
df


# In[136]:


nw_id = pd.Categorical(df["MarriedID"])
nw_id = nw_id.rename_categories(["Unmarried","Married"])



nw_id.describe()


# In[137]:


df["MarriedID"] = nw_id


# In[139]:


df.hist(column = "Salary", figsize = (9,5), bins = 10)


# In[141]:


df.plot(kind = 'scatter', x = 'Sex', y = 'Salary')


# In[142]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




