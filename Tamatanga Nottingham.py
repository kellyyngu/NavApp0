#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = "https://tamatanga.com/menus/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


response = requests.get(url)


# In[5]:


if response.status_code == 200:
    print("Page accessed successfully.")
    page_content = response.content


# In[6]:


soup = BeautifulSoup(page_content, "html.parser")


# In[7]:


menu_sections = soup.find_all('div', class_='menu-items')


# In[8]:


for section in menu_sections:
       item_name = section.find('div') 
       if item_name:
           item_name = item_name.get_text(strip=True)
       print(f"Item: {item_name}")
else:
   print("Failed to retrieve the webpage.")


# In[ ]:




