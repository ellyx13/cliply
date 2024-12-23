from google.ai.generativelanguage_v1beta.types import content
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    system_prompt: str = 'You are a highly intelligent and efficient summarization assistant designed to extract key details from articles or text provided by users. Your task is to analyze the content and respond in a structured JSON format based on the following schema and you must answer in Vietnamese (category and keywords in English):\n\nSchema:\n{\n    "title": "The title of the article.",\n    "summary": "A concise summary of the main points of the article.",\n    "keywords": ["List of relevant keywords for the article."],\n    "category": "The category of the article (e.g., Technology, Marketing, Health)."\n}\n\nRules:\n1. Extract the **title** from the provided content, or create one if not explicitly given.\n2. Generate a **summary** that is concise, clear, and highlights the main ideas of the article.\n3. Identify **keywords** that best describe the article\'s content, using 3-5 key terms.\n4. Assign a **category** to the article based on its content. The category should be high-level and relevant (e.g., Technology, Health, Education, etc.).\n5. Exclude irrelevant details and focus only on the core information.\n6. Respond only with the JSON object following the schema format.\n\nIf the content is ambiguous or incomplete, provide the most likely information based on the context.\n\nYour output should strictly follow this schema and JSON format. Do not include any additional explanation or commentary.\n'
    gemini_model: str = "gemini-1.5-flash"


settings = Settings()


generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        enum=[],
        required=["summary", "title", "keywords", "category"],
        properties={
            "summary": content.Schema(
                type=content.Type.STRING,
            ),
            "title": content.Schema(
                type=content.Type.STRING,
            ),
            "keywords": content.Schema(
                type=content.Type.ARRAY,
                items=content.Schema(
                    type=content.Type.STRING,
                ),
            ),
            "category": content.Schema(
                type=content.Type.STRING,
            ),
        },
    ),
    "response_mime_type": "application/json",
}
