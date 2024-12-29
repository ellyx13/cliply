from loguru import logger
from modules.v1.articles.model import Articles
from telebot.async_telebot import AsyncTeleBot

from .config import settings


class BaseForwarders:
    def __init__(self, bot_token: str, group_id: str):
        self.bot_token = bot_token
        self.group_id = group_id
        self.bot = AsyncTeleBot(self.bot_token)

    def convert_to_slugs(self, text: str):
        return text.lower().replace(" ", "-")

    async def send(self, message: str):
        try:
            await self.bot.send_message(self.group_id, message)
        except Exception as e:
            logger.error(f"Error sending message to Telegram: {e}")


class ForwarderServices(BaseForwarders):
    def __init__(self, bot_token, group_id):
        super().__init__(bot_token, group_id)

    async def send_summary(self, article: Articles):
        category = self.convert_to_slugs(article.category)
        message = f"{article.title}\n\n{article.summary}\n\nKeywords: {', '.join(article.keywords)}\n\nLink: {article.url}\n\n#{category}"
        await self.send(message=message)


forwarder_services = ForwarderServices(bot_token=settings.telegram_bot_token, group_id=settings.telegram_devforce_group_id)
