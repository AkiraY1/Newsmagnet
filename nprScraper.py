import requests
from bs4 import BeautifulSoup

def scrapeNPR(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', id='storytext')
    paragraphs = content.find_all('p')
    return paragraphs