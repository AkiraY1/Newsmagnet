import requests
from bs4 import BeautifulSoup

def scrapeJazeera(URL):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='article-p-wrapper')
    paragraphs = content.find_all('p')
    return paragraphs