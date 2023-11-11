
import requests

def fetch_html_from_url(url):
    """ Fetch HTML content from a URL. """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to download the file. Error code:", response.status_code)
        return None

def read_html_from_file(file_path):
    """ Read HTML content from a local file. """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found:", file_path)
        return None
