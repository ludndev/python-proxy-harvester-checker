class SourceInterface:
    """Interface for defining proxy sources."""

    def __init__(self):
        """Initialize the proxy list."""
        self.proxies = []

    def get_data(self) -> list:
        """
        Fetch data from the proxy source.

        This method should be overridden by subclasses to retrieve data,
        including proxies, from the source.

        Returns:
            list: A list of proxies fetched from the source.
        """
        pass

    def get_proxies(self) -> list:
        """
        Get the list of proxies.

        Calls the get_data method to retrieve proxies and returns them.

        Returns:
            list: A list of proxies.
        """
        self.get_data()
        return self.proxies
