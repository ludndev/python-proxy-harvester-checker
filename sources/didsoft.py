import requests
from sources.interface_source import SourceInterface


class DidSoftSource(SourceInterface):
    """
    A proxy source for fetching proxies from didsoft.com.

    Args:
        email (str): The email address used for authentication.
        password (str): The password used for authentication.
        url (str): The URL to fetch proxies from. If not provided, it will be constructed using the email and password.

    Raises:
        Exception: If email and password are not provided when `url` is None or empty.
    """

    def __init__(self, email=None, password=None, url=None):
        """
        Initialize the DidSoftSource instance.

        Args:
            email (str): The email address used for authentication.
            password (str): The password used for authentication.
            url (str): The URL to fetch proxies from. If not provided, it will be constructed using the email and password.
        """
        super().__init__()
        self.auth = True
        self.url = url
        self.email = email
        self.password = password

    def get_data(self) -> list:
        """
        Fetch data from the DidSoft proxy source.

        This method retrieves proxy data from the DidSoft proxy source.

        Returns:
            list: A list of proxies fetched from the source.
        Raises:
            Exception: If email and password are not provided when `url` is None or empty.
        """
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
