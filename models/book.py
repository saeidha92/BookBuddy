from abc import ABC, abstractmethod



class Readable(ABC):

    @abstractmethod
    def mark_read_page(self, pages:int):
        raise NotImplementedError

    @abstractmethod
    def reading_progress(self):
        raise NotImplementedError

    