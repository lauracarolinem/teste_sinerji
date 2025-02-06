from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
    
# Alerta customizável 
class NotifyUser(Observer):
    def update(self, message):
        print(f"[ALERTA] {message}")