from proxy_checker import ProxyChecker
import signal
import sources


def main():
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


def handler(signum, frame):
    print(f"Received SIGINT signal. Houston, we are going back home ...")
    exit(1)


signal.signal(signal.SIGINT, handler)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Houston, some nasty alien said something. {e}")
