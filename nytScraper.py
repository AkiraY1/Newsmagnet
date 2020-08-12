import requests
from bs4 import BeautifulSoup

def scrapeNYT(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('section', itemprop='articleBody')
    paragraphs = content.find_all('p', class_='css-158dogj evys1bk0')
    return paragraphs