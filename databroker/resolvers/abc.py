
from urllib.parse import urlparse

from abc import ABC,abstractmethod

class Resolver(ABC):
    def __init__(self,uri):
        self.uri = urlparse(uri)

    @abstractmethod
    def get(self,uri:str):
        pass
