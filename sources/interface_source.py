import util


class SourceInterface:
    def __init__(self):
        self.proxies = []

    def get_data(self) -> list:
        pass

    def get_proxies(self) -> list:
        for raw_proxy in self.get_data():
            self.proxies.append(util.build_proxy_dict(raw_proxy))
        return self.proxies
