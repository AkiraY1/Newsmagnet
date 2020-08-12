import requests
from bs4 import BeautifulSoup

def scrapeUSA(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    paragraphs = soup.find_all('p', class_='gnt_ar_b_p')
    return paragraphs