from config import settings
from modules.v1.menu.commands import menu_commands
from modules.v1.start.commands import start_commands
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.telegram_bot_token)


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    result = await start_commands.get_description()
    menu = await menu_commands.get_default_menu()
    await bot.send_message(message.chat.id, result, reply_markup=menu, parse_mode=settings.parse_mode)
