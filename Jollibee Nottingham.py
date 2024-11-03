from bs4 import BeautifulSoup
import requests
import pandas as pd

def fetch_jollibee_menu(url):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        print("Page accessed successfully.")

        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the menu sections
        menu_sections = soup.find_all('div', class_='row sqs-row')

        # Extract item names
        for section in menu_sections:
            item_name = section.find('div') 
            if item_name:
                item_name = item_name.get_text(strip=True)
                print(f"Item: {item_name}")
            else:
                print("No item found in this section.")
                
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve the webpage:", e)

if __name__ == "__main__":
    url = "https://www.jollibee.uk/menu"
    fetch_jollibee_menu(url)
