
# coding: utf-8

# [**Using this guide**:](http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/)

# [**And more importantly this guide**](http://savvastjortjoglou.com/nba-draft-part01-scraping.html)

# In[1]:

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import numpy as np


# In[ ]:



# In[2]:

#Test url: 
#https://docs.google.com/spreadsheets/d/17bMR5x7I13fd6-7Yv-l_nYHtarZdhN58rP79r8k6p70/pubhtml

# Scrape the HTML at the url
url = input("Google Sheets URL: ")

html = urlopen(str(url))


# In[3]:

soup = BeautifulSoup(html, "lxml") 


# In[4]:

soup.findAll('td')


# Found the column names

# In[6]:

column_number = int(input("How many columns? "))

soup.findAll('td', limit = column_number)


# In[7]:

column_headers = [td.getText() for td in 
                  soup.findAll('td', limit = column_number)]


# In[8]:

column_headers


# skip the first 12 header rows

# In[9]:

data_rows = soup.findAll('td')[column_number*2:]
type(data_rows)


# In[10]:

data_rows


# In[11]:

employee_info = []
for td in data_rows:
    td.getText()
    employee_info.append(td.getText())


# In[12]:

employee_info


# In[13]:

i=0
listed_employees=[]
while i<len(employee_info):
  listed_employees.append(employee_info[i:i+column_number])
  i+=column_number

listed_employees


# In[14]:

df = pd.DataFrame(listed_employees, columns=column_headers)


# Getting rid of duplicates

# In[41]:

df = df.drop_duplicates(subset = "Name", keep ="first")


# In[54]:

df


# removing bottom two extra rows

# In[60]:

df = df.iloc[:len(df)-2]

df


# In[64]:

df.head(5)


# In[62]:

df.dtypes


# In[18]:

df = df.convert_objects(convert_numeric=True)
df.dtypes


# In[68]:

cols = list(df.columns.values)
cols


# In[71]:

df = df[['Fiscal Year','Name','Primary Title','Annual Salary at Full FTE','State Fund Ratio','College Name','Department']]

df


# Exporting CSV to fix college names in 14-15 FY

# In[72]:
output_name = input("What should the file be named? ")

df.to_csv(str(output_name)+'.csv')


# In[ ]:



