import requests
from bs4 import BeautifulSoup

def scrapePolitico(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    paragraphs = soup.find_all('p', class_='story-text__paragraph')
    return paragraphs