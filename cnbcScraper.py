import requests
from bs4 import BeautifulSoup

def scrapeCNBC(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find('div', class_='ArticleBody-articleBody')
    if content == None:
        return None
    groups = content.find_all('div', class_='group')
    return groups