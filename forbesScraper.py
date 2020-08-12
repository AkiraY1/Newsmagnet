import requests
from bs4 import BeautifulSoup

def scrapeForbes(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='main-content main-content--desktop-article main-content--universal-header')
    content1 = content.find('div', class_='article-body fs-article fs-responsive-text current-article')
    try:
        paragraphs = content1.find_all('p')
    except:
        return None
    return paragraphs