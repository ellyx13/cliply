from config import settings
from modules.v1.menu.commands import menu_commands


class StartCommands:
    def __init__(self):
        pass

    async def handle_messages(self, bot, message):
        result = await start_commands.get_description()
        menu = await menu_commands.get_default_menu()
        await bot.send_message(message.chat.id, result, reply_markup=menu, parse_mode=settings.parse_mode)

    async def get_description(self):
        description = (
            "Welcome to <b>Cliply</b>!\n\n"
            "Cliply is a Telegram bot designed to help users save, summarize, and share articles effortlessly.\n\n"
            "<b>Features:</b>\n"
            "- <b>/summary</b>: Send a link to summarize its content into a concise overview.\n"
            "- <b>/save_article</b>: Save an article link to your personal library for future access.\n"
            "- <b>/search_articles</b>: Search for saved articles by keywords or topics.\n"
            "- <b>/categorize</b>: Automatically categorize saved articles based on their content.\n"
            "- <b>/share_to_group</b>: Share a saved article (with a summary) to a specified Telegram group.\n"
            "- <b>/weekly_digest</b>: Get a weekly compilation of all saved articles and summaries.\n"
            "- <b>/help</b>: Display detailed instructions on how to use each feature.\n\n"
            "Use the buttons below to interact with the bot, or type the commands directly."
        )
        return description


start_commands = StartCommands()
