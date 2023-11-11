
from bs4 import BeautifulSoup

def html_to_soup(html_content):
    """
    Converts HTML content string to a BeautifulSoup object.

    Parameters:
    html_content (str): HTML content as a string.

    Returns:
    BeautifulSoup: BeautifulSoup object parsed from the HTML content.
    """
    return BeautifulSoup(html_content, 'html.parser')
