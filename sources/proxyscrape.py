import requests
from sources.interface_source import SourceInterface


class ProxyScrapeSource(SourceInterface):
    def get_data(self) -> list:
        url = ("https://api.proxyscrape.com/v3/free-proxy-list/get"
               "?request=displayproxies&protocol=http&proxy_format=ipport&format=json")
        response = requests.get(url)
        self.proxies = []
        if response.status_code == 200:
            data = response.json()
            if 'proxies' in data and len(data['proxies']) > 0:
                for proxy in data['proxies']:
                    secure = 'True' if proxy['ssl'] else 'False'
                    self.proxies.append(f"{proxy['protocol']}|{secure}|{proxy['ip']}:{proxy['port']}")
        else:
            print("Failed to retrieve content from api.proxyscrape.com. Status code:", response.status_code)
        return self.proxies
