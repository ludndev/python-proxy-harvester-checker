import os
import random
import requests
import util
from pathlib import Path
from sources.interface_source import SourceInterface


class ProxyChecker:
    def __init__(self, source=None, file_name="data/proxy_list.txt", validity="https://google.com/"):
        self.proxy_list = []
        self.source = source
        self.file_name = file_name
        self.validity = validity
        self.create_proxy_stored_file_name_if_not_exist()

    def create_proxy_stored_file_name_if_not_exist(self):
        if not os.path.exists(self.file_name):
            Path(self.file_name).touch()

    def check_validity(self):
        return (isinstance(self.validity, str)
                and self.validity != ""
                and self.validity.startswith("http"))

    def harvest_proxy_list(self, source=None):
        if isinstance(source, list):
            for src in source:
                self.harvest_proxy_list(src)
            return

        if isinstance(source, SourceInterface):
            self.proxy_list.extend(source.get_proxies())
            return

    def check_proxy(self, raw_proxy, user_agent=None):
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
        with open(self.file_name, 'r+') as f:
            proxy_list = [line.strip() for line in f]
            f.close()
            return proxy_list

    def store_proxy_list(self):
        with open(self.file_name, 'a+') as f:
            lines = f.readlines()
            for raw_proxy in self.proxy_list:
                proxy_check = self.check_proxy(raw_proxy) if self.check_validity() else True
                if raw_proxy not in lines and proxy_check:
                    f.write(raw_proxy + '\n')
            f.close()

    def get_random_proxy(self):
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
        self.harvest_proxy_list(self.source)
        self.store_proxy_list()
