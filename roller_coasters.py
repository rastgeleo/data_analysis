#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


wood = pd.read_csv('data/Golden_Ticket_Award_Winners_Wood.csv')
wood.head()


# In[6]:


steel = pd.read_csv('data/Golden_Ticket_Award_Winners_Steel.csv')
steel.head()


# In[26]:


def plot_rank(ax, df, name, park_name, marker='o'):
    df_byname = df[(df.Name == name) & (df.Park == park_name)].reset_index()

    out = plt.plot('Year of Rank', 'Rank', data=df_byname, marker=marker)
    
    ax.set_title("Rakings")
    ax.set_xlabel("Year")
    ax.set_ylabel("Ranking")
    
    ax.invert_yaxis()
    ax.set_yticks(df_byname['Rank'].values)
    
    return out


# In[27]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_rank(ax, wood, "El Toro", "Six Flags Great Adventure")


# In[31]:


def plot_rank_fortwo(ax, df, name1, park_name1, name2, park_name2, marker='o'):
    df1_byname_park = df[(df.Name == name1) & (df.Park == park_name1)].reset_index()
    df2_byname_park = df[(df.Name == name2) & (df.Park == park_name2)].reset_index()

    ax.plot('Year of Rank', 'Rank', data=df1_byname_park, marker=marker) 
    ax.plot('Year of Rank', 'Rank', data=df2_byname_park, marker=marker)
    
    ax.set_title("Rakings")
    ax.set_xlabel("Year")
    ax.set_ylabel("Ranking")
    ax.legend(["{}".format(name1), "{}".format(name2)])
    
    ax.invert_yaxis()
    ax.set_yticks(df1_byname_park['Rank'].values)
    
    return None


# In[32]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_rank_fortwo(ax, wood, "El Toro", "Six Flags Great Adventure", "The Voyage", "Holiday World")


# In[ ]:


def plot_topn(ax, df, n, marker='o'):
    top_ranked = df[df.Rank <= n]
    roller_coasters = top_ranked.Name.unique()
    for roller_coaster in roller_coasters:
        data = top_ranked[top_ranked.Name == roller_coaster]
        ax.plot('Year of Rank', 'Rank', data=data, label=roller_coaster, marker=marker)
    
    ax.legend(roller_coasters, loc='best')
    ax.set_title("Top ranked roller coasters each year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Rank")
    ax.set_yticks(range(n))
    ax.invert_yaxis()


# In[89]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_topn(ax ,wood, 5)


# In[42]:


roller_coasters = pd.read_csv('data/roller_coasters.csv')
roller_coasters.head()


# In[43]:


def plot_hist(ax, df, col_name):
    df = df.dropna()
    if col_name == 'height':
        df = df[df[col_name] <= 140]
    out = ax.hist(col_name, data=df, alpha=0.5)
    
    ax.set_title("{} distribution".format(col_name.replace('_', ' ').title()))
    ax.set_xlabel("height")
    ax.set_ylabel("number of roller coasters")
    
    return out
    


# In[44]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_hist(ax, roller_coasters, 'height')


# In[46]:


def plot_bar_inversion(ax, df, park_name):
    df_bypark_name = df[df.park == park_name]
    x = range(df_bypark_name['name'].shape[0])
    y = df_bypark_name['num_inversions'].values
    ax.bar(x, y)
    
    ax.set_title('Number of Inversion per Roller Coaster')
    ax.set_xlabel('Roller Coasters')
    ax.set_ylabel('Number of Inversions')
    
    ax.set_xticks(x)
    ax.set_xticklabels(df_bypark_name['name'], rotation=70, horizontalalignment='right')
    


# In[48]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_bar_inversion(ax, roller_coasters, 'Parc Asterix')


# In[68]:


def plot_pie(ax, df):
    df_operating = df[df.status == 'status.operating']
    df_closed = df[df.status == 'status.closed.definitely']

    size = [df_operating.shape[0], df_closed.shape[0]]
    labels = ["operating", "closed"]
    
    ax.pie(size, labels=labels, autopct='%1.1f%%', colors=['purple', 'pink'])
    
    ax.set_title("Operating vs Closed Rollercoasters")
    


# In[69]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_pie(ax, roller_coasters)


# In[90]:


def plot_scatter(ax, df, col_1, col_2):
    
    if 'height' in [col_1, col_2]:
        df = df[df.height <= 140]
 
    out = ax.scatter(col_1, col_2, data=df, color='gray')
    ax.set_title("Relationship between height and speed of Roller Coasters")
    ax.set_xlabel(col_1)
    ax.set_ylabel(col_2)
    
    return out


# In[91]:


fig, ax = plt.subplots(figsize=(8, 5))
plot_scatter(ax, roller_coasters, 'speed', 'height')


# In[ ]:




