#!/usr/bin/env python
# coding: utf-8

# In[53]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[54]:


url = "https://www.jollibee.uk/menu"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[55]:


print(soup)


# In[56]:


response = requests.get(url)


# In[57]:


if response.status_code == 200:
    print("Page accessed successfully.")
    page_content = response.content


# In[58]:


soup = BeautifulSoup(page_content, "html.parser")


# In[59]:


menu_sections = soup.find_all('div', class_='row sqs-row')


# In[60]:


for section in menu_sections:
       item_name = section.find('div') 
       if item_name:
           item_name = item_name.get_text(strip=True)
       print(f"Item: {item_name}")
else:
   print("Failed to retrieve the webpage.")


# In[ ]:




