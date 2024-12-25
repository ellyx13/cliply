from urllib.parse import urlparse


class Articles:
    def __init__(self, url: str = None, title: str = None, content: str = None, summary: str = None, keywords: list = None, category: str = None):
        """
        Initialize the Articles object from input data.

        :param url: URL of the article (required).
        :param title: Title of the article (default None).
        :param summary: Summary of the article (default None).
        :param content: Content of the article (default None).
        :param keywords: List of keywords (default None).
        :param category: Category of the article (default None).
        :param created_at: Time of article creation (default None).
        """
        if not isinstance(keywords, list):
            raise ValueError("Keywords must be a list")

        self.url = url
        self.domain = self.get_domain(url)
        self.title = title
        self.summary = summary
        self.content = content
        self.keywords = keywords or []
        self.category = category

    def get_domain(self, url: str):
        """
        Get the domain from the URL.
        """
        return urlparse(url).netloc

    @classmethod
    def from_summary(cls, summary: dict, content: str = None, url: str = None):
        """
        Create an Articles object from a summary dictionary.
        """
        return cls(
            url=url,
            title=summary["title"],
            content=content,
            summary=summary["summary"],
            keywords=summary["keywords"],
            category=summary["category"],
        )

    def to_dict(self):
        """
        Convert the Articles object to a dictionary.
        """
        return {
            "url": self.url,
            "domain": self.domain,
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "keywords": self.keywords,
            "category": self.category,
        }
