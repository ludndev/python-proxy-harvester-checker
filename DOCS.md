# Technical Documentation

## Proxy Checker

The `ProxyChecker` class provides functionality to harvest, check, and manage proxies from various sources.

### Usage

```python
from proxy_checker import ProxyChecker
import sources

# Create an instance of ProxyChecker with default configurations
proxy_checker = ProxyChecker()

# Harvest proxies from specific sources
ssl_proxies_source = sources.SslProxiesSource()
proxy_scrape_source = sources.ProxyScrapeSource()

# Configure ProxyChecker with specific sources and validity URL
proxy_checker_configured = ProxyChecker(
    source=[ssl_proxies_source, proxy_scrape_source],
    file_name="data/new_year_proxy.txt",
    validity="https://google.com/"
)

# Perform the proxy harvesting, checking, and storing operation
proxy_checker_configured.do_the_thing()

# Retrieve the list of valid proxies
proxies = proxy_checker_configured.get_proxy_list()

# Print the total number of proxies obtained
print(f"Total number of proxies: {len(proxies)}")

# Use a specific proxy for making requests
random_proxy = proxy_checker_configured.get_random_proxy()
print(f"Random proxy: {random_proxy}")
```

### Example

#### Use Case

In a web scraping application, you need to scrape data from multiple websites without getting blocked. You decide to use proxies to avoid IP bans and increase your scraping efficiency.
In this use case, we want to scrap data from AliExpress.

#### Configuration

You configure the `ProxyChecker` with two proxy sources: `SslProxiesSource` and `ProxyScrapeSource`, and set the validity URL to "https://example.com/" to check the validity of proxies.

```python
from proxy_checker import ProxyChecker
import sources

# Create instances of proxy sources
ssl_proxies_source = sources.SslProxiesSource()
proxy_scrape_source = sources.ProxyScrapeSource()

# Configure ProxyChecker with specific sources and validity URL
proxy_checker = ProxyChecker(
    source=[ssl_proxies_source, proxy_scrape_source],
    validity="https://aliexpress.com/"
)

# Perform the proxy harvesting, checking, and storing operation
proxy_checker.do_the_thing()
```

### Parameters

- `source`: A list of proxy sources or a single instance of `SourceInterface`.
- `file_name`: The name of the file to store valid proxies (default: "data/proxy_list.txt").
- `validity`: The URL to check the validity of proxies (default: "https://google.com/").

### Methods

- `create_proxy_stored_file_name_if_not_exist()`: Create the proxy storage file if it does not exist.
- `check_validity()`: Check if the validity URL is valid.
- `harvest_proxy_list(source)`: Harvest proxies from the specified source(s).
- `check_proxy(raw_proxy, user_agent)`: Check the validity of a proxy.
- `get_proxy_list()`: Get the list of valid proxies from the storage file.
- `store_proxy_list()`: Store valid proxies in the storage file.
- `get_random_proxy()`: Get a random valid proxy from the storage file.
- `do_the_thing()`: Perform the main operation: harvest, store, and check proxies.

## Examples

### Example 1: Basic Configuration

In this example, we create a basic configuration of `ProxyChecker` with default settings. We just want to get a list of valid proxy from all available sources.

```python
from proxy_checker import ProxyChecker

# Create an instance of ProxyChecker with default configurations
proxy_checker = ProxyChecker()

# Perform the proxy harvesting, checking, and storing operation
proxy_checker.do_the_thing()

# Retrieve the list of valid proxies
proxies = proxy_checker.get_proxy_list()

# Print the total number of proxies obtained
print(f"Total number of proxies: {len(proxies)}")
```

### Example 2: Custom Configuration

In this example, we configure `ProxyChecker` with specific proxy sources and a validity URL.

```python
from proxy_checker import ProxyChecker
import sources

# Create instances of proxy sources
ssl_proxies_source = sources.SslProxiesSource()
proxy_scrape_source = sources.ProxyScrapeSource()

# Configure ProxyChecker with specific sources and validity URL
proxy_checker = ProxyChecker(
    source=[ssl_proxies_source, proxy_scrape_source],
    validity="https://example.com/"
)

# Perform the proxy harvesting, checking, and storing operation
proxy_checker.do_the_thing()

# Retrieve the list of valid proxies
proxies = proxy_checker.get_proxy_list()

# Print the total number of proxies obtained
print(f"Total number of proxies: {len(proxies)}")
```

### Example 3: Random Proxy

In this example, we suppose that you have a valid proxy list in `data/proxy_list.txt`. We will pick a proxy randomly.

```python
from proxy_checker import ProxyChecker
import sources

# Create instances of proxy sources
ssl_proxies_source = sources.SslProxiesSource()
proxy_scrape_source = sources.ProxyScrapeSource()

# Create an instance of ProxyChecker with default configurations
proxy_checker = ProxyChecker()

# Randomly select a from proxy list and return a build proxy dict
proxy = proxy_checker.get_random_proxy()

# Print the total number of proxies obtained
print(f"Request proxy : {proxy}")
```

This technical documentation provides detailed information about the `ProxyChecker` class, its usage, parameters, methods, and examples of different configurations. Users can refer to this documentation to understand how to use the `ProxyChecker` class effectively in their applications.
