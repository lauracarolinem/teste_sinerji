from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class QueryLLMCommand(Command):
    def __init__(self, client, question):
        self.client = client
        self.question = question
        
    def execute(self):
        return self.client.send_request(self.question)