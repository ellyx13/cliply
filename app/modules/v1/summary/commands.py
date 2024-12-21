import re


class SummaryCommands:
    def __init__(self):
        pass

    def extract_link(self, text: str):
        url_pattern = r"(https?://[^\s]+)"
        links = re.findall(url_pattern, text)
        if links:
            return links[0]
        return None

    async def handle_messages(self, bot, message):
        link = self.extract_link(message.text)
        if link is None:
            return None
        await bot.send_message(message.chat.id, f"Link: {link}")


summary_commands = SummaryCommands()
