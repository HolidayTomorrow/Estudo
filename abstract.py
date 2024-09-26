from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg) -> None: ...
    
    def log_error(self, msg) -> str:
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg) -> str:
        return self._log(f'Success: {msg}')
        
        
class LogPrintMixin(Log):
    def _log(self, msg) -> str:
        print(f'{msg} ({self.__class__.__name__})')
        
        
        
        
l = LogPrintMixin()
l.log_error('Erro ao chamar a função')