import unittest
import sources


class TestProxySources(unittest.TestCase):
    def setUp(self):
        self.proxies = {}

    def test_get_proxies_from_all_sources(self):
        sources_classes = sources.get_sources(auth=None)
        self.fetch_and_assert_proxies(sources_classes)

    def test_get_proxies_with_auth_true(self):
        sources_classes = sources.get_sources(auth=True)
        self.fetch_and_assert_proxies(sources_classes)

    def test_get_proxies_with_auth_false(self):
        sources_classes = sources.get_sources(auth=False)
        self.fetch_and_assert_proxies(sources_classes)

    def fetch_and_assert_proxies(self, sources_classes):
        for source_class in sources_classes:
            source_instance = source_class()
            if source_class.__name__ not in self.proxies:
                self.proxies[source_class.__name__] = source_instance.get_proxies()
        for source in self.proxies.keys():
            # Assert that the total number of proxies retrieved is greater than zero
            self.assertGreater(len(self.proxies[source]), 0)


if __name__ == '__main__':
    unittest.main()
