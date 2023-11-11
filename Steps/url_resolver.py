
from urllib.parse import urlparse
from collections import defaultdict
from url_utils import extract_original_url


def resolve_facebook_urls(url_list):
    """
    Resolves Facebook redirect URLs to their original URLs.

    Parameters:
    url_list (list): A list of URLs to resolve.

    Returns:
    list: A list of resolved URLs.
    """
    resolved_urls = []
    for url in url_list:
        if urlparse(url).netloc in ['l.facebook.com', 'lm.facebook.com']:
            original_url = extract_original_url(url)
            resolved_urls.append(original_url)
        else:
            resolved_urls.append(url)
    return resolved_urls


def count_domain_statistics(url_list):
    """
    Counts the occurrences of each domain in the URL list.

    Parameters:
    url_list (list): A list of URLs.

    Returns:
    dict: A dictionary with domains as keys and counts as values.
    """
    domain_counts = defaultdict(int)
    for url in url_list:
        domain = urlparse(url).netloc
        domain_counts[domain] += 1
    return dict(sorted(domain_counts.items(), key=lambda item: item[1], reverse=True))
