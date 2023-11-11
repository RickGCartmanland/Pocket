
from collections import defaultdict
from urllib.parse import urlparse
from Steps.url_extractor import extract_original_url


def count_domains(all_domain_urls):
    """
    Counts the number of URLs for each domain, resolving Facebook URLs to their original domains.

    Args:
    all_domain_urls (dict): A dictionary with domains as keys and list of URLs as values.

    Returns:
    dict: A dictionary with domains as keys and the count of URLs as values, sorted by count in descending order.
    """
    original_domain_counts = defaultdict(int)
    for domain, urls in all_domain_urls.items():
        if domain in ['l.facebook.com', 'lm.facebook.com']:
            for fb_url in urls:
                original_url = extract_original_url(fb_url)
                if original_url:
                    original_domain = urlparse(original_url).netloc
                    original_domain_counts[original_domain] += 1
        else:
            original_domain_counts[domain] += len(urls)

    return dict(sorted(original_domain_counts.items(), key=lambda item: item[1], reverse=True))
