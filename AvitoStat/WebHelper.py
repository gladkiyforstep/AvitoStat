import requests
from bs4 import BeautifulSoup


class WebHelper:
    def __init__(self, query: str, region: str):
        self.url = "https://www.avito.ru/{}?q={}".format(region, query)
        self.html = self.get_html()
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_count(self) -> int:
        count = self.soup.findAll('span', class_='page-title-count-1oJOc')
        print(count)
        return int(count[0].text.replace(' ', ''))

