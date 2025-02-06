from abc import ABC, abstractmethod
from difflib import SequenceMatcher

class ResponseEvaluation(ABC):
    @abstractmethod
    def evaluation (self, question, gpt_answer, gem_answer):
        pass
    
# Usa similaridade para comparar a resposta com a pergunta feita
class SimilarityStrategy(ResponseEvaluation):
    def evaluation(self, question, gpt_answer, gem_answer):
        gpt_result = SequenceMatcher(None, question, gpt_answer).ratio()
        gem_result = SequenceMatcher(None, question, gem_answer).ratio()
        if gpt_result > gem_result:
            return -1
        elif gem_result > gpt_result:
            return 1
        else:
            return 0
        
# # É uma comparação simples, mas compara o tamanho da pergunta com o tamanho das respostas
# class LenghtComparisonStrategy(ResponseEvaluation):
#     def evaluation(self, question, gpt_answer, gem_answer):
#         good_size = len(question) * 2
        
#         gpt_result = abs(len(gpt_answer) - good_size)
#         gem_result = abs(len(gem_answer) - good_size)
        
#         if gpt_result > gem_result:
#             return -1
#         elif gem_result > gpt_result:
#             return 1
#         else:
#             return 0

# Contexto que permite a mudança de estratégias ao longo do programa 
class StrategyContext:
    def __init__(self, strategy: ResponseEvaluation):
        self.strategy = strategy
    
    def set_strategy(self, strategy: ResponseEvaluation):
        self.strategy = strategy
    
    def process_responses(self, question, gpt_answer, gem_answer):
        result = self.strategy.evaluation(question, gpt_answer, gem_answer)
        if result == -1:
            return "A resposta do GPT foi melhor"
        elif result == 1:
            return "A resposta do Gemini foi melhor"
        else:
            return "Empate"
        
        