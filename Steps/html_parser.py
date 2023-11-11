
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import defaultdict

def parse_html_file(file_path):
    """
    Parses an HTML file and groups URLs by their domain.
    
    Args:
    file_path (str): Path to the HTML file.
    
    Returns:
    defaultdict(list): A dictionary with domains as keys and list of URLs as values.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    all_domain_urls = defaultdict(list)
    for link in soup.find_all('a', href=True):
        url = link.get('href')
        domain = urlparse(url).netloc
        all_domain_urls[domain].append(url)
    
    return all_domain_urls
