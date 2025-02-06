from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from google import genai

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
_ = load_dotenv(find_dotenv())

class APIClient(ABC):
    @abstractmethod
    def send_request(self, prompt):
        pass
    
class ChatGptClient(APIClient):
    def send_request(self, prompt):
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
            {"role": "user", 
            "content": prompt}
            ]
        )
        return completion.choices[0].message
        
class GeminiClient(APIClient):
    def send_request(self, prompt):
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
        )
        return response.text
        
class APIClientFactory:
    @staticmethod
    def create_client(model):
        if model == "chatgpt":
            return ChatGptClient()
        elif model == "gemini":
            return GeminiClient()
        else:
            raise ValueError("Modelo não encontrado")