from bs4 import BeautifulSoup
import requests
import pandas as pd

def fetch_pizza_hut_menu(url):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        print("Page accessed successfully.")

        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the menu sections
        menu_sections = soup.find_all('div', class_='col-12 pb-3 menu-products')

        # Extract item names
        if menu_sections:
            for section in menu_sections:
                item_name_div = section.find('div') 
                if item_name_div: 
                    item_name = item_name_div.get_text(strip=True)
                    print(f"Item: {item_name}") 
        else:
            print("No menu sections found.")

    except requests.exceptions.RequestException as e:
        print("Failed to retrieve the webpage:", e)

if __name__ == "__main__":
    url = "https://www.pizzahut.co.uk/restaurants/find/menu/nottinghamcastlemeadow"
    fetch_pizza_hut_menu(url)
