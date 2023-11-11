
# Adjust the import as per your project structure
from Steps.url_extractor import extract_original_url
from urllib.parse import urlparse


def resolve_facebook_in_domains(all_domain_urls):
    """
    Resolves Facebook URLs to their original URLs within the all_domain_urls dictionary.

    Parameters:
    all_domain_urls (dict): A dictionary mapping domains to lists of URLs.

    Returns:
    dict: A dictionary similar to all_domain_urls but with Facebook URLs resolved.
    """
    resolved_urls = {}
    for domain, urls in all_domain_urls.items():
        resolved_domain_urls = []
        for url in urls:
            if urlparse(url).netloc in ['l.facebook.com', 'lm.facebook.com']:
                original_url = extract_original_url(url)
                resolved_domain_urls.append(
                    original_url if original_url else url)
            else:
                resolved_domain_urls.append(url)
        resolved_urls[domain] = resolved_domain_urls
    return resolved_urls
