from bs4 import BeautifulSoup
import requests

def fetch_mem_saab_menu(url):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        print("Page accessed successfully.")

        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the menu sections
        menu_sections = soup.find_all('div', class_='tabbed')

        # Extract item names
        if menu_sections:
            for section in menu_sections:
                item_name = section.find('div')
                if item_name:
                    item_name = item_name.get_text(strip=True)
                    print(f"Item: {item_name}")
                else:
                    print("No item name found in this section.")
        else:
            print("No menu sections found.")

    except requests.exceptions.RequestException as e:
        print("Failed to retrieve the webpage:", e)

if __name__ == "__main__":
    url = "https://www.mem-saab.co.uk/menus/"
    fetch_mem_saab_menu(url)
