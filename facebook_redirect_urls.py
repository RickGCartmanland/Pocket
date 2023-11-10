from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urlparse
from collections import defaultdict
import os


def extract_original_url(fb_url):
    parsed_url = urllib.parse.urlparse(fb_url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return query_params.get('u', [None])[0]


# Fájl elérési útja
html_file_path = 'ril_export.html'

# HTML fájl beolvasása és elemzése
with open(html_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Összes URL kinyerése és csoportosítása
all_domain_urls = defaultdict(list)
for link in soup.find_all('a', href=True):
    url = link.get('href')
    domain = urlparse(url).netloc
    all_domain_urls[domain].append(url)

# Facebook URL-ek feloldása és az összes URL hozzáadása
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

# Domainek és URL számok rendezése
sorted_original_domain_counts = dict(
    sorted(original_domain_counts.items(), key=lambda item: item[1], reverse=True))

# Eredmény megjelenítése
print(sorted_original_domain_counts)
