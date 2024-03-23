import requests
from bs4 import BeautifulSoup
from sources.interface_source import SourceInterface


class SslProxiesSource(SourceInterface):
    """
    A proxy source for fetching proxies from www.sslproxies.org.

    This class implements the SourceInterface and fetches proxies from the SSL Proxies website.

    Attributes:
        proxies (list): A list to store the fetched proxies.
    """

    def get_data(self):
        """
        Fetch data from the SSL Proxies proxy source.

        This method retrieves proxy data from the SSL Proxies website.

        Returns:
            list: A list of proxies fetched from the source.
        """
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
