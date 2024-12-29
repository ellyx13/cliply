from config import settings
from modules.v1.start.commands import start_commands
from modules.v1.summary.commands import summary_commands
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.telegram_bot_token)


async def check_authorization(message, ignore_send_message=False):
    if message.from_user.username != settings.telegram_admin_username:
        if ignore_send_message:
            return False
        unauthorized_message = "You are not authorized to use this bot."
        await bot.send_message(message.chat.id, unauthorized_message)
        return False
    return True


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    if await check_authorization(message):
        await start_commands.handle_messages(bot, message)


@bot.message_handler(func=lambda message: True)  # Xử lý mọi tin nhắn gửi đến bot
async def handle_messages(message):
    if await check_authorization(message, ignore_send_message=True):
        await summary_commands.handle_messages(message)


@bot.message_handler(commands=["summary"])  # Xử lý mọi tin nhắn gửi đến bot
async def summary(message):
    if await check_authorization(message):
        await summary_commands.handle_messages(message)
