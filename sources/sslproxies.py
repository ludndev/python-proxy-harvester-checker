import requests
import util
from bs4 import BeautifulSoup
from sources.interface_source import SourceInterface


class SslProxiesSource(SourceInterface):
    def get_data(self):
        response = requests.get("https://www.sslproxies.org/")
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.select_one('table', class_='.table .table-striped .table-bordered')
        if table:
            tbody = table.select_one('tbody')
            for row in tbody.find_all('tr')[1:]:
                columns = row.find_all('td')
                ip = columns[0].text
                port = columns[1].text
                secure = 'False'
                self.proxies.append(f'http|{secure}|{ip}:{port}')
        return self.proxies
