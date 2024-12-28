import re

from loguru import logger
from modules.v1.articles.object import Articles
from modules.v1.articles.services import article_services
from modules.v1.crawler.services import crawler_services
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

    def convert_to_slugs(self, text: str):
        return text.lower().replace(" ", "-")

    async def send_summary(self, bot, message, article: Articles):
        category = self.convert_to_slugs(article.category)
        summary = f"{article.title}\n\n{article.summary}\n\nKeywords: {', '.join(article.keywords)}\n\nLink: {article.url}\n\n#{category}"
        await bot.send_message(message.chat.id, summary)

    async def handle_messages(self, bot, message):
        link = self.extract_link(message.text)
        if link is None:
            return None
        logger.info(f"Extracted content in link: {link}")
        summary = await article_services.get_by_url(link)
        if summary:
            await self.send_summary(bot, message, article=summary)
            return None
        title = crawler_services.get_title(link)
        content = crawler_services.get_full_content(link)
        logger.info(f"Summarizing {title} ...")
        summary = await gemini_services.chat(content)
        article = Articles.from_summary(summary=summary, content=content, url=link)
        await article_services.create(article)
        await self.send_summary(bot, message, article=article)


summary_commands = SummaryCommands()
