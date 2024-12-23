import json

import google.generativeai as genai

from .config import generation_config, settings


class GeminiServices:
    def __init__(self, model: str, api_key: str, system_prompt: str, generation_config: dict):
        self.model = model
        self.api_key = api_key
        self.system_prompt = system_prompt
        genai.configure(api_key=self.api_key)

        self.gemini = genai.GenerativeModel(
            model_name=self.model,
            generation_config=generation_config,
            system_instruction=self.system_prompt,
        )

    async def chat(self, prompt: str):
        chat_session = self.gemini.start_chat()
        response = chat_session.send_message(prompt)
        response_json = json.loads(response.text)
        return response_json


gemini_services = GeminiServices(settings.gemini_model, settings.GEMINI_API_KEY, settings.system_prompt, generation_config)
