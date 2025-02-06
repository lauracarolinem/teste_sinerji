from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from google import genai

_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

class APIClient(ABC):
    @abstractmethod
    def send_request(self, question):
        pass
    
class ChatGptClient(APIClient):
    def send_request(self, question):
        client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
            {"role": "user", 
            "content": question}
            ]
        )
        gpt_response = completion.choices[0].message.content
        return gpt_response
        
class GeminiClient(APIClient):
    def send_request(self, question):
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=question
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