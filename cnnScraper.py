import requests
from bs4 import BeautifulSoup

def scrapeCNN(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    content6 = soup.find('div', class_='pg-rail-tall__wrapper')
    if content6 == None:
        contents = soup.find_all('div', class_='Paragraph__component')
    else:
        content1 = soup.find('div', class_= 'zn-body__read-all')
        if content1 == None:
            return None
        contents = content1.find_all('div', class_= 'zn-body__paragraph')
    return contents