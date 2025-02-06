from clientFactory import APIClientFactory
from commands import QueryLLMCommand

if __name__ == "__main__":
  question = input("Pergunta: ")
  
  # Cria a conexão com as LLM's
  clientGPT = APIClientFactory.create_client("chatgpt")
  clientGem = APIClientFactory.create_client("gemini")
  
  # Inicializa os comandos
  command_gpt = QueryLLMCommand(clientGPT, question)
  command_gem = QueryLLMCommand(clientGem, question)
  
  # Executa os comandos 
  response_from_gpt = command_gpt.execute()
  response_from_gem = command_gem.execute()
  
  # Respostas
  print("Chat GPT: \n" + response_from_gem)
  print("---------------------------------------------------------------------------------------")
  print("Gemini: \n" + response_from_gpt)

