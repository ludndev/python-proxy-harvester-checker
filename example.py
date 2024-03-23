from proxy_checker import ProxyChecker
import sources


source = sources.SslProxiesSource()
print(f"Proxies: {len(source.get_proxies())} in {source.__class__.__name__}")

source = sources.ProxyScrapeSource()
print(f"Proxies: {len(source.get_proxies())} in {source.__class__.__name__}")

# source = sources.DidSoftSource(email="email@example.com", password="password")
# print(f"Proxies: {len(source.get_proxies())} in {source.__class__.__name__}")


proxy_checker = ProxyChecker([
    sources.SslProxiesSource(),
    sources.ProxyScrapeSource(),
])

proxy_checker.do_the_thing()

proxies = proxy_checker.get_proxy_list()

print(f"Proxies: {len(proxies)} in many `sources`")
