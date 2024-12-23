import requests
from bs4 import BeautifulSoup
from loguru import logger


class CrawlerServices:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    def _fetch_content(self, url):
        """Fetches the webpage content and stores it in a BeautifulSoup object."""
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")
        logger.info(f"Failed to fetch content from {url}")
        return None

    def get_title(self, url):
        """Extracts and returns the title of the webpage."""
        soup = self._fetch_content(url)
        if soup is None or soup.title is None:
            return None
        return soup.title.string

    def _extract_content(self, soup):
        """Extracts and returns all <h1> to <h6> and <p> tags in order."""
        content = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"])
        return [element.get_text() for element in content]

    def get_full_content(self, url):
        """Returns the title and content combined."""
        soup = self._fetch_content(url)
        if soup is None:
            return None
        content = self._extract_content(soup)
        return "\n".join(content)


crawler_services = CrawlerServices()
