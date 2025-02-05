from google import genai
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
#pip install openai
#pip install -U google-generativeai

_ = load_dotenv(find_dotenv())
question = input("Pergunta: ")


# #GEMINI
# GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# client = genai.Client(api_key=GEMINI_API_KEY)
# response = client.models.generate_content(
#     model="gemini-2.0-flash", 
#     contents=question
# )
# print(response.text)


#CHAT-GPT    
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
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

print(completion.choices[0].message);
