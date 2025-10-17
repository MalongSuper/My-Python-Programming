# Analyze URLs - Ranking in Search Engine
import requests
import random
from bs4 import BeautifulSoup

# List of URLs
url_1 = 'https://www.deviantart.com'
url_2 = 'https://www.youtube.com'
url_3 = 'https://www.reddit.com'
url_4 = 'https://www.apple.com'
url_5 = 'https://www.pinterest.com'
url_6 = 'https://www.reddit.com'


def fetch_page(url):
    """Fetch the HTML content of the webpage."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page. Status code: {response.status_code}")


def analyze_page(html_content):
    """Analyze the HTML content for SEO elements."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title tag
    title = soup.title.string if soup.title else 'No title tag found'

    # Extract meta description
    meta_description = ''
    description_tag = soup.find('meta', attrs={'name': 'description'})
    if description_tag:
        meta_description = description_tag.get('content', 'No description content found')

    # Extract H1 tags
    h1_tags = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]

    # Extract URLs
    urls = [a.get('href') for a in soup.find_all('a', href=True)]

    # Extract other header tags
    headers = {
        'h2': [h2.get_text(strip=True) for h2 in soup.find_all('h2')],
        'h3': [h3.get_text(strip=True) for h3 in soup.find_all('h3')],
        'h4': [h4.get_text(strip=True) for h4 in soup.find_all('h4')],
        'h5': [h5.get_text(strip=True) for h5 in soup.find_all('h5')],
        'h6': [h6.get_text(strip=True) for h6 in soup.find_all('h6')],
    }

    return {
        'title': title,
        'meta_description': meta_description,
        'h1_tags': h1_tags,
        'urls': urls,
        'headers': headers
    }


def main():
    url_list = [url_1, url_2, url_3, url_4, url_5, url_6]
    url = random.choice(url_list)
    html_content = fetch_page(url)
    seo_elements = analyze_page(html_content)

    # Display the extracted SEO elements
    print("Search Engine")
    print("Title Tag:", seo_elements['title'])
    print("Meta Description:", seo_elements['meta_description'])
    print("H1 Tags:", seo_elements['h1_tags'])
    print("Header Tags:", seo_elements['headers'])
    print("URLs on the page:")
    for seo in seo_elements['urls']:
        print(seo)


main()
