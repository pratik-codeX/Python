from abc import ABC,abstractmethod  #Abstract Base Class

class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class Derived(Base):    
    

dobj = Derived()    #Error