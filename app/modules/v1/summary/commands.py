import re

from loguru import logger
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

    async def send_summary(self, bot, message, title, content, keyword, category, link):
        category = self.convert_to_slugs(category)
        summary = f"{title}\n\n{content}\n\nKeywords: {', '.join(keyword)}\n\nLink: {link}\n\n#{category}"
        await bot.send_message(message.chat.id, summary)

    async def handle_messages(self, bot, message):
        link = self.extract_link(message.text)
        if link is None:
            return None
        logger.info(f"Extracted content in link: {link}")
        title = crawler_services.get_title(link)
        content = crawler_services.get_full_content(link)
        logger.info(f"Summarizing {title} ...")
        article = await gemini_services.chat(content)
        await self.send_summary(bot, message, article["title"], article["summary"], article["keywords"], article["category"], link)


summary_commands = SummaryCommands()
