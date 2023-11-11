from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import defaultdict


def extract_urls(soup):
    """
    Extracts all URLs from the BeautifulSoup parsed HTML.

    Parameters:
    soup (BeautifulSoup): Parsed HTML content.

    Returns:
    list: A list of URLs extracted from the HTML.
    """
    return [link.get('href') for link in soup.find_all('a', href=True)]


def group_urls_by_domain(url_list):
    """
    Groups URLs by their domain.

    Parameters:
    url_list (list): A list of URLs.

    Returns:
    dict: A dictionary mapping domains to lists of URLs.
    """
    domain_urls = defaultdict(list)
    for url in url_list:
        domain = urlparse(url).netloc
        domain_urls[domain].append(url)
    return domain_urls
