#!/usr/bin/env python
# coding: utf-8

# # <h1><center>Data Science - Data Visualisation with Altair</center></h1>

# In[1]:


# • Go to: https://www.kaggle.com/datasets 

# • Select a dataset

# • Then create a data dashboard using Altair or Tableau  https://public.tableau.com/en-us/s/ 

# • Then create a markdown cell explain why you have decided on the design choices, what influenced your decisions and what 
# insights have you found from the data.


# In[2]:


import altair as alt
import pandas as pd
import numpy as np


# In[3]:


dataset = pd.read_csv (r'C:\Users\sudip\holiday_destination.csv')
print (dataset)


# In[4]:


# Size of Dataset


# In[5]:


print(dataset.shape)


# In[6]:


# Top 5 Rows


# In[7]:


dataset.head(5)


# In[8]:


# The statistical details of the dataset using describe().


# In[9]:


dataset.describe()


# In[10]:


# Plotting and Creating Charts


# In[11]:


alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='most_visited_city',
    color='feedback_score'
).interactive()


# In[12]:


alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='holiday_destination',
    color='most_visited_city'
).interactive()


# In[13]:


alt.Chart(dataset).mark_point().encode(
    x='average_review_score', 
    y='holiday_destination',
    size='hotel_star_rating',
).interactive()


# In[14]:


barPlot = alt.Chart(dataset).mark_bar().encode(
    x='all_inclusive_package', 
    y='holiday_destination',
    size ='hotel_star_rating',
    color='hotel_star_rating:N'
).interactive()
barPlot


# In[15]:


circlePlot = alt.Chart(dataset).mark_circle().encode(
    x='all_inclusive_package', 
    y='holiday_destination',
    size = 'hotel_star_rating',
    color='hotel_star_rating:N',
    tooltip=['country','feedback_score'],
).interactive()
circlePlot


# In[16]:


stackbarPlot = alt.Chart(dataset).mark_bar().encode(
    x='average_review_score', 
    y='country',
    color='hotel_star_rating:N',
    tooltip=['holiday_destination', 'hotel_star_rating']

)
stackbarPlot


# In[18]:


# I found Data Visualisation module very challenging, initially found various datasets on kaggle and tried to use Tableau, 
# however even after using the guide and YouTube tips, I still found it quite difficult to use it. Then, I attempted the Altair
# method, so far it's much easier to understand. I chose an easier dataset, following the holiday destination homework in Pandas
# but adding more details then converting it into a CSV file. When I tried importing my file, I kept receiving a unicode error,
# after some research and going through my files, I've found that converting my regular CSV file to a CSV-UTF-8 fixed the 
# unicode error I kept receiving on Jupyter Notebook. After researching on some graphs, I really loved the look of circlePlot
# and stackbarPlot, however I knew because I don't have much data to work with, for the most parts it will look incomplete. 
# If I were to do this again, I would keep the feedback_score and hotel_star_rating balanced rather than just keeping the 
# values really high, so the graphs would not feel incomplete. 

