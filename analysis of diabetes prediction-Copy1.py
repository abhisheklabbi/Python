#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# In[3]:


df = pd.read_csv("diabetes2.csv")
df


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


print(df.isnull().any().sum())
print(df.isnull().sum())


# In[8]:


#removing zero values
df=df[-(df[df.columns[1:-1]] == 0).any(axis=1)]
df.shape


# In[9]:


#histogram plots
for i,col in enumerate(df.columns[:-1]):
    plt.figure(i)
    sn.distplot(df[col]);


# In[ ]:





# In[11]:


df.corr()


# In[12]:


plt.figure(figsize=(9,9))
sn.heatmap(np.abs(df.corr()), annot= True, cmap="viridis",fmt="0.2f");


# In[ ]:


#and you can see this is a symmetrik matrix  too.but it immidietly allows us to point out the most correlated and 
#anti-correlated
#attributes some might just be common sence -pregnencies v/s age example but some might give us real insight into the data 
#it allows tosee what we need to investigate and which variable we need to focus on if we donot have the time and resourses 
# to investigate every possible colimn.


# In[ ]:





# In[26]:


#2D histogram
plt.figure(figsize=(10,9))
plt.hist2d(df["Glucose"],df["BMI"],bins=(20,20), cmap="magma")
plt.xlable("Glucose")
plt.ylable("BMI")
plt.colorbar();


# In[19]:


plt.figure(figsize=(9,9))
m= df["Outcome"]==1

plt.scatter(df.loc[m,"Glucose"], df.loc[m,"BMI"], c="r", s=15 )
plt.scatter(df.loc[-m,"Glucose"], df.loc[-m,"BMI"], c="b", s=15)
plt.x("Glucose")
plt.y("BMI")
plt.legend(loc=2);


# In[ ]:


# x axis = Gluose
# y axis = BMI
#Red = Diabetic
#blue =Non-Diabetic


# In[20]:


df=df[["Glucose","BMI","Age","Outcome"]]


# In[17]:


df.shape


# In[ ]:


import seaborn as sn


# In[16]:


sn.distplot(df["Age"])


# In[24]:


sn.countplot(x='Glucose', data=df)


# In[ ]:





# In[ ]:




