
from collections import defaultdict
from urllib.parse import urlparse


def count_domain_statistics(url_list):
    """
    Counts the occurrences of each domain in the URL list.

    Parameters:
    url_list (list): A list of URLs.

    Returns:
    dict: A dictionary with domains as keys and counts as values, sorted by count.
    """
    domain_counts = defaultdict(int)
    for url in url_list:
        domain = urlparse(url).netloc
        domain_counts[domain] += 1
    return dict(sorted(domain_counts.items(), key=lambda item: item[1], reverse=True))


def count_domain_statistics(grouped_urls):
    stats = {}
    for domain, urls in grouped_urls.items():
        # Count the number of URLs for each domain
        stats[domain] = len(urls)
    return stats
