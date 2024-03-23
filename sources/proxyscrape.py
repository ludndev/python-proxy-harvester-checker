import requests
from interface_source import SourceInterface


class ProxyScrapeSource(SourceInterface):
    def get_data(self) -> list:
        url = ("https://api.proxyscrape.com/v3/free-proxy-list/get"
               "?request=displayproxies&protocol=http&proxy_format=ipport&format=json")
        response = requests.get(url)
        proxies = []
        if response.status_code == 200:
            data = response.json()
            if 'proxies' in data and len(data['proxies']) > 0:
                for proxy in data['proxies']:
                    secure = 'True' if proxy['ssl'] else 'False'
                    proxies.append(f"{proxy['protocol']}|{secure}|{proxy['ip']}:{proxy['port']}")
        else:
            print("Failed to retrieve content from api.proxyscrape.com. Status code:", response.status_code)
        return proxies

    def get_proxies(self) -> list:
        for raw_proxy in self.get_data():
            self.proxies.append(self.build_proxy_dict(raw_proxy))
        return self.proxies
