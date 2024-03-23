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

    def build_proxy_dict(self, raw_proxy):
        proxy_dict = {}

        raw_dict = raw_proxy.split('|')

        if raw_dict[0] != 'socks4' and raw_dict[0] != 'socks5':
            proxy_dict['http'] = f'https://{raw_dict[2]}'
            if raw_dict[1] == 'True':
                proxy_dict['https'] = f'https://{raw_dict[2]}'

        if raw_dict[0] == 'socks4':
            proxy_dict['http'] = f'socks4://{raw_dict[2]}'
            if raw_dict[1] == 'True':
                proxy_dict['https'] = f'socks4://{raw_dict[2]}'

        if raw_dict[0] == 'socks5':
            proxy_dict['http'] = f'socks5://{raw_dict[2]}'
            if raw_dict[1] == 'True':
                proxy_dict['https'] = f'socks5://{raw_dict[2]}'

        return proxy_dict

    def get_proxy_list(self):
        with open(self.file_name, 'r+') as f:
            proxy_list = [line.strip() for line in f]
            f.close()
            return proxy_list
