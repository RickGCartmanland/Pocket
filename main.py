
from Steps.html_parser import parse_html_file
from Steps.domain_counter import count_domains


def main():
    """
    Main function to parse HTML file and count URL domains.
    """
    html_file_path = 'ril_export.html'
    all_domain_urls = parse_html_file(html_file_path)
    sorted_original_domain_counts = count_domains(all_domain_urls)
    print(sorted_original_domain_counts)


if __name__ == "__main__":
    main()
