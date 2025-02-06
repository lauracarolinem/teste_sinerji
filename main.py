from clientFactory import APIClientFactory
from commands import QueryLLMCommand
from strategies import *
from observer import NotifyUser


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

  print("\n")
  # Usando o Observer para notificar que a melhor resposta foi escolhida
  notify = NotifyUser()
  notify.update("A melhor resposta foi escolhida")
  
  # Comparações para avaliar a melhor resposta de acordo com a estratégia de similaridade entre a pergunta e a resposta
  context = StrategyContext(SimilarityStrategy())
  best_answer = context.process_responses(question, response_from_gpt, response_from_gem)

  print(best_answer)