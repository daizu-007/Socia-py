from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class Model:
    def __init__(self):
        GOOGLE_AI_API_KEY = os.environ.get("GOOGLE_AI_API_KEY")
        GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
        GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
        self.google = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=GOOGLE_AI_API_KEY)
        self.github = OpenAI(base_url="https://models.inference.ai.azure.com", api_key=GITHUB_TOKEN)
        self.groq = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)

    def add_system_message(self, chat, message):
        chat.append({"role": "system", "content": message})

    def add_user_message(self, chat, message):
        chat.append({"role": "user", "content": message})

    def add_bot_message(self, chat, message):
        chat.append({"role": "assistant", "content": message})

    def google_chat_completion(self, chat):
        response = self.google.chat.completions.create(
            messages=chat,
            model="gemini-2.0-flash-exp",
        )
        return response.choices[0].message.content

    def github_chat_completion(self, chat):
        response = self.github.chat.completions.create(
            messages=chat,
            model="gpt-4o-mini",
        )
        return response.choices[0].message.content

    def groq_chat_completion(self, chat):
        response = self.groq.chat.completions.create(
            messages=chat,
            model="deepseek-r1-distill-llama-70b",
        )
        return response.choices[0].message.content