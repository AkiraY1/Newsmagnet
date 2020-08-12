import requests
from bs4 import BeautifulSoup

def scrapeHill(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='field-item even')
    paragraphs = content.find_all('p')
    return paragraphs