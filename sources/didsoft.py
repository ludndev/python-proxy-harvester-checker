import requests
from sources.interface_source import SourceInterface


class DidSoftSource(SourceInterface):
    def get_data(self, email=None, password=None, url=None) -> list:
        if url is None or url == "":
            if email is None or password is None:
                raise Exception("Email and password are required for didsoft.com proxy source")
            url = ("http://list.didsoft.com/get"
                   f"?email={email}.com&pass={password}&pid=http1000&showcountry=no")
        response = requests.get(url)
        if response.status_code == 200:
            for line in response.content.splitlines():
                self.proxies.append(f"http|false|{line.strip()}")
        else:
            print("Failed to retrieve content from list.didsoft.com. Status code:", response.status_code)
        return self.proxies
