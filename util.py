def build_proxy_dict(raw_proxy):
    """
    Build a dictionary representation of a raw proxy string.

    This function parses a raw proxy string and constructs a dictionary representation
    containing the proxy details suitable for use with the `requests` library.

    Args:
        raw_proxy (str): The raw proxy string in the format 'protocol|secure|ip:port'.

    Returns:
        dict: A dictionary containing the proxy details.
    """
    proxy_dict = {}

    raw_dict = raw_proxy.split('|')

    if raw_dict[0] != 'socks4' and raw_dict[0] != 'socks5':
        proxy_dict['http'] = f'http://{raw_dict[2]}'
        if raw_dict[1] == 'True':
            proxy_dict['http'] = f'https://{raw_dict[2]}'
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
