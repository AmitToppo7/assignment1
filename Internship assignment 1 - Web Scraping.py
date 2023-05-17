#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Installing_Libraries

import requests
from bs4 import BeautifulSoup 
import pandas as pd


# In[2]:


url = "http://quotes.toscrape.com/"


# In[3]:


#Collecting_response

response = requests.get(url)


# In[4]:


#Display the content

response.content


# In[5]:


Soup = BeautifulSoup(response.content,'html.parser')


# In[6]:


#Find div 

div = Soup.find('div')


# In[7]:


quotes = div.find_all('div', class_ = 'quote')


# In[8]:


#declaring a list to store the data

Q = []


# In[9]:


for quote in quotes:
    txt = quote.find('span', class_ = "text").text
    author = quote.find('small', class_ = "author").text
    tag = quote.find('meta', attrs={'class': 'keywords'})
    keywords = tag['content'].split(',')
    
    Q.append([txt,author,keywords])
    


# In[10]:


#Process for all the pages

Q = []

for i in range(1,12):
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    response.content
    Soup = BeautifulSoup(response.content,'html.parser')
    div = Soup.find('div')
    quotes = div.find_all('div', class_ = 'quote')
    
    for quote in quotes:
        txt = quote.find('span', class_ = "text").text
        author = quote.find('small', class_ = "author").text
        tag = quote.find('meta', attrs={'class': 'keywords'})
        keywords = tag['content'].split(',')
    
        Q.append([txt,author,keywords])
        
        print(Q)
        


# In[11]:


df = pd.DataFrame(Q, columns = ['Quote', 'Author', 'Tags'])
print(df)


# In[12]:


def save_to_csv(df, filename):
    # Save DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f'Saved DataFrame to {filename}')


# In[13]:


save_to_csv(df,'Quotestoscrape.txt')


# In[ ]:




