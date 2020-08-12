import requests
from bs4 import BeautifulSoup

def scrapeGuardian(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    paragraphs = soup.find_all('p', class_='css-182kmce')
    return paragraphs