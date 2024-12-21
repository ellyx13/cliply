import asyncio
import datetime
import sys

from config import settings
from controllers import bot
from loguru import logger

# Setup logger
logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {level} | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <level>{message}</level>")
logger.add(settings.log_path, colorize=False, format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {level} | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <level>{message}</level>", rotation=datetime.time(0, 0, 0, tzinfo=datetime.timezone.utc))


async def main():
    logger.info("Starting bot")
    await bot.polling()


asyncio.run(main())
