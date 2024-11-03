from bs4 import BeautifulSoup
import requests

def fetch_mcdonalds_menu(url):
    try:
        # Send a request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful requests
        print("Page accessed successfully.")

        # Parse the page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the menu sections
        menu_sections = soup.find_all('div', class_='menu-categories aem-GridColumn--default--9 aem-GridColumn')
        
        # Extract item names from the first section
        if menu_sections:
            for section in menu_sections:
                item_name = section.find('div') 
                if item_name:
                    item_name = item_name.get_text(strip=True)
                    print(f"Item: {item_name}")
                else:
                    print("No item name found in this section.")

        # Find additional menu sections
        menu_sections_2 = soup.find_all('div', class_='category-container container responsivegrid cmp-container--fixed pt-responsive cmp-container--padding aem-GridColumn aem-GridColumn--default--12')
        
        # Extract item names from the second section
        if menu_sections_2:
            for section in menu_sections_2:
                item_name = section.find('div') 
                if item_name:
                    item_name = item_name.get_text(strip=True)
                    print(f"Item: {item_name}")
                else:
                    print("No item name found in this section.")
        else:
            print("No additional menu sections found.")

    except requests.exceptions.RequestException as e:
        print("Failed to retrieve the webpage:", e)

if __name__ == "__main__":
    url = "https://www.mcdonalds.com/gb/en-gb/menu.html"
    fetch_mcdonalds_menu(url)
