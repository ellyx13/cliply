from config import settings
from modules.v1.start.commands import start_commands
from modules.v1.summary.commands import summary_commands
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.telegram_bot_token)


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    await start_commands.handle_messages(bot, message)


@bot.message_handler(func=lambda message: True)  # Xử lý mọi tin nhắn gửi đến bot
async def handle_messages(message):
    await summary_commands.handle_messages(bot, message)


@bot.message_handler(commands=["summary"])  # Xử lý mọi tin nhắn gửi đến bot
async def summary(message):
    await summary_commands.handle_messages(bot, message)
