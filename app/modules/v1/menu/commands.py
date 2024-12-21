from telebot.types import KeyboardButton, ReplyKeyboardMarkup


class MenuCommands:
    def __init__(self):
        pass

    async def get_default_menu(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        markup.add(
            KeyboardButton("/summary"),
            KeyboardButton("/save_article"),
            KeyboardButton("/search_articles"),
        )
        markup.add(
            KeyboardButton("/categorize"),
            KeyboardButton("/share_to_group"),
            KeyboardButton("/weekly_digest"),
        )
        markup.add(KeyboardButton("/help"))
        return markup


menu_commands = MenuCommands()
