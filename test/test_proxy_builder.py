import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util import build_proxy_dict


class TestProxyBuilder(unittest.TestCase):
    def test_build_proxy_dict_http(self):
        # Test building proxy dictionary for HTTP proxy
        proxy = 'http|False|127.0.0.1:8080'
        expected_result = {'http': 'http://127.0.0.1:8080'}
        self.assertEqual(build_proxy_dict(proxy), expected_result)

    def test_build_proxy_dict_https(self):
        # Test building proxy dictionary for HTTPS proxy
        proxy = 'http|True|127.0.0.1:8080'
        expected_result = {'http': 'https://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
        self.assertEqual(build_proxy_dict(proxy), expected_result)


if __name__ == '__main__':
    unittest.main()
