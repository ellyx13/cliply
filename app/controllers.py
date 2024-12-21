from config import settings
from modules.v1.start.commands import start_commands
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.telegram_bot_token)


@bot.message_handler(commands=["start"])
async def send_welcome(message):
    result = await start_commands.run()
    await bot.reply_to(message, result)
