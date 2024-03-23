from proxy_checker import ProxyChecker
import signal
import sources


def main():
    """
    The main function to harvest, check, and manage proxies.

    This function orchestrates the proxy harvesting, checking, and management process.
    It fetches proxies from different sources, checks their validity, stores valid proxies,
    and prints the total number of proxies obtained from all sources.

    Raises:
        Exception: If an error occurs during the proxy harvesting or checking process.
    """
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
    """
    Signal handler function for SIGINT (Ctrl+C) signal.

    Args:
        signum (int): The signal number.
        frame (frame): The current stack frame.
    """
    print(f"Received SIGINT signal. Houston, we are going back home ...")
    exit(1)


signal.signal(signal.SIGINT, handler)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Houston, some nasty alien said something. {e}")
