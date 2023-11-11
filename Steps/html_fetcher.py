
import requests
from bs4 import BeautifulSoup

def fetch_and_parse_html(url):
    """
    Fetches an HTML file from the given URL and parses it with BeautifulSoup.

    Parameters:
    url (str): URL of the HTML file to fetch.

    Returns:
    BeautifulSoup object: Parsed HTML content, or None if the fetch was unsuccessful.
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup
    else:
        print("Failed to download the file. Error code:", response.status_code)
        return None
