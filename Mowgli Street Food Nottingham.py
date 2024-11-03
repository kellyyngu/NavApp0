#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = "https://www.mowglistreetfood.com/menus/nottingham/food/"
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


# In[8]:


menu_sections = soup.find_all('div', class_='wp-block-columns has-3-columns menu-section is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex')


# In[9]:


for section in menu_sections:
       item_name = section.find('div') 
       if item_name:
           item_name = item_name.get_text(strip=True)
       print(f"Item: {item_name}")
else:
   print("Failed to retrieve the webpage.")

