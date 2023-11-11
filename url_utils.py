
"""
Utility functions for URL processing.
"""

from urllib.parse import urlparse, parse_qs

def extract_original_url(fb_url):
    """
    Extract the original URL from a Facebook redirect URL.
    
    Parameters:
    fb_url (str): The Facebook redirect URL.

    Returns:
    str: The original URL if present, otherwise None.
    """
    parsed_url = urlparse(fb_url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('u', [None])[0]
