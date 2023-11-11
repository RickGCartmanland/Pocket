from Steps.html_fetcher import fetch_html_from_url, read_html_from_file
from Steps.html_parser import extract_urls, group_urls_by_domain
from Steps.html_to_soup import html_to_soup
from Steps.domain_statistics import count_domain_statistics
from Steps.url_resolver import resolve_facebook_urls


def main():
    """
    Main function to parse HTML file and count URL domains.
    """

    url = 'https://raw.githubusercontent.com/RickGCartmanland/Pocket/main/ril_export.html'
    html_content = fetch_html_from_url(url)
    soap = html_to_soup(html_content)
    raw_urls = extract_urls(soap)
    all_urls = resolve_facebook_urls(raw_urls)
    grouped_urls = group_urls_by_domain(all_urls)
    stats = count_domain_statistics(grouped_urls)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted statistics
    for domain, count in sorted_stats:
        print(f"{domain}: {count}")


if __name__ == "__main__":
    main()
