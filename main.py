from clientFactory import APIClientFactory
from commands import QueryLLMCommand

if __name__ == "__main__":
  question = input("Pergunta: ")
  
  clientGPT = APIClientFactory.create_client("chatgpt")
  clientGem = APIClientFactory.create_client("gemini")
  
  command_gpt = QueryLLMCommand(clientGPT, question)
  command_gem = QueryLLMCommand(clientGem, question)
  
  raw_response_from_gpt = command_gpt.execute()
  raw_response_from_gem = command_gem.execute()
  
  print("Chat GPT: \n" + raw_response_from_gem)
  print("---------------------------------------------------------------------------------------")
  print("Gemini: \n" + raw_response_from_gpt)

