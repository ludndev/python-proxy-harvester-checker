# Python Proxy Harvester and Checker

![Python version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This Python project provides a simple yet powerful solution for harvesting and checking proxy servers from various sources. It includes functionality to fetch proxies from different online sources, check their validity, and store valid proxies for later use.

## Features

- **Proxy Harvester**: Fetch proxies from multiple online sources such as ProxyScrape and others.
- **Proxy Checker**: Verify the validity of proxies by making test requests to a specified URL.
- **Storage**: Store valid proxies in a file for later use in your applications.
- **Flexible Architecture**: Easily extendable with new proxy sources by implementing the `SourceInterface`.
- **CLI Interface**: Command-line interface for easy interaction and integration into scripts.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ludndev/python-proxy-harvester-checker.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the example script to harvest and check proxies:

   ```bash
   python example.py
   ```

4. Integrate the `ProxyChecker` class into your own projects for proxy management.

## Configuration

- `proxy_checker.py`: Contains the `ProxyChecker` class responsible for proxy harvesting, checking, and storing.
- `sources/`: Directory containing implementations of proxy sources, each implementing the `SourceInterface`.
- `data/`: Directory where valid proxies are stored. (Note: `proxy_list.txt` is ignored by default in `.gitignore`)

## Contributing

Contributions to this project are welcome! If you have any ideas for new features, bug fixes, or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
