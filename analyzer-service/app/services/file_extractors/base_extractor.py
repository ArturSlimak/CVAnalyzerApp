from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    @abstractmethod
    def extract_text(self, data: bytes | str) -> str:
        pass
