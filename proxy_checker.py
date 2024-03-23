import os
from pathlib import Path


class ProxyChecker:
    def __init__(self, source=None, file_name="proxy_list.txt", validity="https://google.com/"):
        self.proxy_list = []
        self.source = source
        self.file_name = file_name
        self.validity = validity
        self.create_proxy_stored_file_name_if_not_exist()

    def create_proxy_stored_file_name_if_not_exist(self):
        if not os.path.exists(self.file_name):
            Path(self.file_name).touch()
