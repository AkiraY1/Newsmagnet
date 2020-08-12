import requests
from bs4 import BeautifulSoup

def scrapeFox(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='article-body')
    try:
        paragraphs = content.find_all('p')
    except:
        return None
    return paragraphs