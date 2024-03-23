def build_proxy_dict(raw_proxy):
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
