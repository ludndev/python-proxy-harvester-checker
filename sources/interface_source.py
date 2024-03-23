import util


class SourceInterface:
    def __init__(self):
        self.proxies = []

    def get_data(self) -> list:
        pass

    def get_proxies(self) -> list:
        self.get_data()
        return self.proxies
