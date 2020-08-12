import requests
from bs4 import BeautifulSoup

def scrapeWashington(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    teaserContent = soup.find('div', class_='teaser-content')
    if teaserContent == None:
        paragraphs = soup.find('p')
        return paragraphs
    else:
        teaserContentText = teaserContent.find('p')
        remainderContent = soup.find('div', class_='remainder-content')
        paragraphs = remainderContent.find_all('p')
        return teaserContentText, paragraphs