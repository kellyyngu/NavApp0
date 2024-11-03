#!/usr/bin/env python
# coding: utf-8

# In[43]:


from bs4 import BeautifulSoup
import requests


# In[44]:


url = "https://www.mcdonalds.com/gb/en-gb/menu.html"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[45]:


print(soup)


# In[46]:


response = requests.get(url)


# In[47]:


if response.status_code == 200:
    print("Page accessed successfully.")
    page_content = response.content


# In[48]:


soup = BeautifulSoup(page_content, "html.parser")


# In[49]:


menu_sections = soup.find_all('div', class_='menu-categories aem-GridColumn--default--9 aem-GridColumn')


# In[50]:


for section in menu_sections:
       item_name = section.find('div') 
       if item_name:
           item_name = item_name.get_text(strip=True)
       print(f"Item: {item_name}")
else:
   print("Failed to retrieve the webpage.")


# In[58]:


menu_sections_2 = soup.find_all('div', class_='category-container container responsivegrid cmp-container--fixed pt-responsive cmp-container--padding aem-GridColumn aem-GridColumn--default--12')


# In[59]:


for section in menu_sections_2:
       item_name = section.find('div') 
       if item_name:
           item_name = item_name.get_text(strip=True)
       print(f"Item: {item_name}")
else:
   print("Failed to retrieve the webpage.")


# In[ ]:




