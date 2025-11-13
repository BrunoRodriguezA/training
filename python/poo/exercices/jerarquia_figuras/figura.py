from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def area(self) -> float:
        ...
        
    @abstractmethod
    def perimetro(self) -> float:
        ...