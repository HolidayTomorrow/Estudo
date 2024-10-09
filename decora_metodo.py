from abc import ABC, abstractmethod

class Nothing(ABC):
    def __init__(self, thing):
        self._thing = None
        self.thing = thing
        
        
    @property
    def nothing(self):
        return self._thing
    
    @nothing.setter
    @abstractmethod
    def nothing(self, thing): ...
    
    
    
class Thing(Nothing):
    def __init__(self, thing):
        super().__init__(thing)
        # print('Nada')
        
        
    @Nothing.nothing.setter
    def nothing(self, thing):
        self._thing = thing
        
        
        
nada = Thing('Nada')
print(nada.nothing)