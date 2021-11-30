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


df =pd.read_csv("boston.csv")
df


# In[4]:


df.head()


# In[5]:


df.describe()


# In[12]:


df.info()


# In[24]:


data.isnull().sum()/len(data)=100


# In[27]:


plt.bar(df.CRIM,df.MEDV)
plt.xlabel('Crime Rtae')
plt.ylable('Price of the House')
plt.title('Crime Rate vs Price of House')
plt.plot()
#AS THE CRIME RATE INCREASES HOUSE RATE DECRESES
# X = CRIME RATE
# Y = PRICE OF HOUSE


# In[28]:


plt.bar(df.INDUS,df.MEDV)
plt.xlabel('Non Retail business proposition')
plt.ylable('Price of House')
plt.title('Non Retail business proportion vs Price of House')
plt.plot()
# X = Non Retail business proposition


# In[29]:


plt.bar(df.NOX,df.MEDV)
plt.xlabel('Nitric oxide Concentration')
plt.ylable('Price of House')
plt.title('Nitric oxide Concentration vs Price of House')
plt.plot()
# as a nitric oxide concentration incrases the price of houses decreases


# In[30]:


plt.bar(df.RM,df.MEDV)
plt.xlabel('Avg nor of rooms')
plt.ylable('Price of House')
plt.title('Avg nor of rooms vs Price of House')
plt.plot()
# nor of rooms increses then price of house also increses


# In[31]:


plt.bar(df.PTRATIO,df.MEDV)
plt.xlabel('Pupil- teacher of ratios')
plt.ylable('Price of House')
plt.title('pupil teacher of ratio vs Price of House')
plt.plot()


# In[32]:


plt.bar(df.LSTAT,df.MEDV)
plt.xlabel('% lower status population')
plt.ylable('Price of House')
plt.title('% lower status population vs Price of House')
plt.plot()
#where the lower state population is low price the price of the houses is high


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:


df.describe().loc["mean"].plot.bar()
plt.show
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


sn.pairplot(df,size=1.5);
plt.show


# In[8]:


col_study =['ZN','INDUS','NOX','RM']


# In[10]:


sn.pairplot(df[col_study],size=2.5);
plt.show()


# In[ ]:




