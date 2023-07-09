import requests
from bs4 import BeautifulSoup



def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main content from the website
    # Customize this code based on the specific website structure

    # Example: Extract all paragraph tags
    paragraphs = soup.find_all('p')

    # Return the extracted content
    return [p.get_text() for p in paragraphs]
