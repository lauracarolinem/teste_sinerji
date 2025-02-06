from apiFactory import APIClientFactory

if __name__ == "__main__":
  question = input("Pergunta: ")
  
  clientGPT = APIClientFactory.create_client("chatgpt")
  clientGem = APIClientFactory.create_client("gemini")
  
  
  