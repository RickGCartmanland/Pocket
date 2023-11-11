
from urllib.parse import urlparse, parse_qs

def extract_original_url(fb_url):
    """
    Extracts the original URL from a Facebook URL.
    
    Args:
    fb_url (str): The Facebook URL to be parsed.
    
    Returns:
    str: The original URL if available, else None.
    """
    parsed_url = urlparse(fb_url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('u', [None])[0]
