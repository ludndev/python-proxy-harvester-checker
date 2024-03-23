import requests
from sources.interface_source import SourceInterface


class DidSoftSource(SourceInterface):
    def __init__(self, email=None, password=None, url=None):
        super().__init__()
        self.url = url
        self.email = email
        self.password = password

    def get_data(self) -> list:
        if self.url is None or self.url == "":
            if self.email is None or self.password is None:
                raise Exception("Email and password are required for didsoft.com proxy source")
            self.url = ("http://list.didsoft.com/get"
                   f"?email={self.email}.com&pass={self.password}&pid=http1000&showcountry=no")
        response = requests.get(self.url)
        if response.status_code == 200:
            for line in response.content.splitlines():
                self.proxies.append(f"http|false|{line.strip()}")
        else:
            print("Failed to retrieve content from list.didsoft.com. Status code:", response.status_code)
        return self.proxies
