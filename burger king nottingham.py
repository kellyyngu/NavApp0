#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[52]:


url = "https://www.pizzahut.co.uk/restaurants/find/menu/nottinghamcastlemeadow"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[53]:


print(soup)


# In[54]:


response = requests.get(url)


# In[55]:


if response.status_code == 200:
    print("Page accessed successfully.")
    page_content = response.content


# In[56]:


soup = BeautifulSoup(page_content, "html.parser")


# In[57]:


menu_sections = soup.find_all('div', class_='col-12 pb-3 menu-products')


# In[58]:


for section in menu_sections:
    item_name_div = section.find('div') 
    if item_name_div: 
        item_name = item_name_div.get_text(strip=True)
        print(f"Item: {item_name}") 
    else:
        print("No item name found in this section.")

if not menu_sections:
    print("Failed to retrieve the webpage.")

