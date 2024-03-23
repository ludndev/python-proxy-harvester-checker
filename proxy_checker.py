
class ProxyChecker:
    def __init__(self, source=None, file_name="proxy_list.txt", validity="https://google.com/"):
        self.proxy_list = []
        self.source = source
        self.file_name = file_name
        self.validity = validity
