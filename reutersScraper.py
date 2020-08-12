import requests
from bs4 import BeautifulSoup

def scrapeReuters(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='StandardArticleBody_body')
    paragraphs = content.find_all('p')
    return paragraphs