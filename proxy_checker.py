import os
import random
import requests
import util
from pathlib import Path
from sources.interface_source import SourceInterface
from sources import get_sources


class ProxyChecker:
    """
    A class for harvesting, checking, and managing proxies.

    This class provides functionality to harvest proxies from various sources,
    check their validity, store valid proxies, and retrieve a random proxy.

    Attributes:
        source (list or SourceInterface, optional): The source(s) from which to harvest proxies.
            Can be a single SourceInterface instance or a list of instances.
        file_name (str, optional): The name of the file to store the valid proxies. Defaults to "data/proxy_list.txt".
        validity (str, optional): The URL to check the validity of proxies. Defaults to "https://google.com/".
    """

    def __init__(self, source=None, file_name="data/proxy_list.txt", validity="https://google.com/"):
        """
        Initialize the ProxyChecker instance.

        Args:
            source (list or SourceInterface, optional): The source(s) from which to harvest proxies.
                Can be a single SourceInterface instance or a list of instances.
            file_name (str, optional): The name of the file to store the valid proxies.
                Defaults to "data/proxy_list.txt".
            validity (str, optional): The URL to check the validity of proxies. Defaults to "https://google.com/".
        """
        self.proxy_list = []
        self.source = source
        self.file_name = file_name
        self.validity = validity
        self.create_proxy_stored_file_name_if_not_exist()

    def create_proxy_stored_file_name_if_not_exist(self):
        """
        Create the proxy storage file if it does not exist.
        """
        if not os.path.exists(self.file_name):
            Path(self.file_name).touch()

    def check_validity(self):
        """
        Check if the validity URL is valid.

        Returns:
            bool: True if the validity URL is valid, False otherwise.
        """
        return (isinstance(self.validity, str)
                and self.validity != ""
                and self.validity.startswith("http"))

    def default_sources(self):
        """Retrieve default sources without authentication.

        Returns:
            list: List of source instances without authentication.
        """
        sources = []
        for source_class in get_sources():
            if not source_class().auth:
                sources.append(source_class())
        return sources

    def harvest_proxy_list(self, source=None):
        """
        Harvest proxies from the specified source(s) or from default sources

        Args:
            source (list or SourceInterface, optional): The source(s) from which to harvest proxies.
                Can be a single SourceInterface instance or a list of instances.
        """
        if source is None:
            self.source = self.default_sources()
            self.harvest_proxy_list(self.source)
            return

        if isinstance(source, list):
            for src in source:
                self.harvest_proxy_list(src)
            return

        if isinstance(source, SourceInterface):
            self.proxy_list.extend(source.get_proxies())
            return

    def check_proxy(self, raw_proxy, user_agent=None):
        """
        Check the validity of a proxy.

        Args:
            raw_proxy (str): The raw proxy string.
            user_agent (str, optional): The user agent string. Defaults to a common user agent string.

        Returns:
            bool: True if the proxy is valid, False otherwise.
        """
        if not isinstance(user_agent, str) or user_agent == "":
            user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3")
        headers = {"User-Agent": user_agent}
        proxies = util.build_proxy_dict(raw_proxy)
        try:
            response = requests.get(self.validity, headers=headers, proxies=proxies, timeout=5)
            if response.status_code == 200:
                return True
        except Exception as e:
            print(f"{str(e)} while checking proxy at {e.__traceback__.tb_lineno}")
            pass
        return False

    def get_proxy_list(self):
        """
        Get the list of valid proxies from the storage file.

        Returns:
            list: A list of valid proxies.
        """
        with open(self.file_name, 'r+') as f:
            proxy_list = [line.strip() for line in f]
            f.close()
            return proxy_list

    def store_proxy_list(self):
        """
        Store valid proxies in the storage file.
        """
        with open(self.file_name, 'a+') as f:
            lines = f.readlines()
            for raw_proxy in self.proxy_list:
                proxy_check = self.check_proxy(raw_proxy) if self.check_validity() else True
                if raw_proxy not in lines and proxy_check:
                    f.write(raw_proxy + '\n')
            f.close()

    def get_random_proxy(self):
        """
        Get a random valid proxy from the storage file.

        Returns:
            dict: A dictionary containing the proxy details (protocol, IP, port).
        """
        with open(self.file_name, 'r+') as f:
            proxy_list = [line.strip() for line in f]
            if len(proxy_list) == 0:
                return None
            random.shuffle(proxy_list)
            for raw_proxy in proxy_list:
                return util.build_proxy_dict(raw_proxy)
            f.close()
        return None

    def do_the_thing(self):
        """
        Perform the main operation: harvest, store, and check proxies.
        """
        self.harvest_proxy_list(self.source)
        self.store_proxy_list()
