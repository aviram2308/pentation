
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


# mfd is mutual fund data df
# cd is client data df
mfd=pd.read_csv('Mutual Fund Data.csv', encoding="ISO-8859-1")


# In[7]:


cd=pd.read_table('Client Data.txt', encoding="ISO-8859-1")


# In[8]:


#summarising mfd and cd
mfd.describe()


# In[9]:


cd.describe()


# In[14]:


# grouping mfd by location, branchcode and brokername
mfd_loc=mfd.groupby('Location')


# In[15]:


for x,y in mfd_loc:
    print(x)
    print(y)


# In[16]:


mfd_bc=mfd.groupby('BranchCode')


# In[17]:


mfd_bc.groups


# In[18]:


mfd_bn=mfd.groupby('BrokerName')


# In[19]:


mfd_bn.groups


# In[20]:


# grouping cd by sex, city name, state name
cd_s=cd.groupby('sex')


# In[21]:


cd_s.groups


# In[22]:


cd_city=cd.groupby('city_name')


# In[23]:


cd_city.groups


# In[24]:


cd_state=cd.groupby('state_name')


# In[25]:


cd_state.groups


# In[27]:


# plotting mfd amount vs location
mfd.plot(y='amount', x='Location')


# In[28]:


#plotting mfd amount vs branchcode
mfd.plot(y='amount', x='BranchCode')


# In[30]:


# renaming the column of cd to Client.Code
cd['Client.Code']=cd['Commonclientcode']


# In[32]:


# merging mfd and cd using client.code column
mergedf=pd.merge(mfd, cd, on='Client.Code')


# In[33]:


#summarising the merged df
mergedf.describe()

