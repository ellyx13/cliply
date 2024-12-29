import re

from loguru import logger
from modules.v1.articles.object import Articles
from modules.v1.articles.services import article_services
from modules.v1.crawler.services import crawler_services
from partners.v1.forwarders.services import forwarder_services
from partners.v1.gemini.services import gemini_services


class SummaryCommands:
    def __init__(self):
        pass

    def extract_link(self, text: str):
        url_pattern = r"(https?://[^\s]+)"
        links = re.findall(url_pattern, text)
        if links:
            return links[0]
        return None

    async def summary(self, link: str) -> Articles:
        title = crawler_services.get_title(link)
        content = crawler_services.get_full_content(link)
        logger.info(f"Summarizing {title} ...")
        summary = await gemini_services.chat(content)
        article = Articles.from_summary(summary=summary, content=content, url=link)
        await article_services.create(article)
        return article

    async def handle_messages(self, message):
        link = self.extract_link(message.text)
        if link is None:
            return None
        logger.info(f"Extracted content in link: {link}")
        article = await article_services.get_by_url(link)
        if article:
            await forwarder_services.send_summary(article=article)
            return None
        article = await self.summary(link)
        await forwarder_services.send_summary(article=article)


summary_commands = SummaryCommands()
