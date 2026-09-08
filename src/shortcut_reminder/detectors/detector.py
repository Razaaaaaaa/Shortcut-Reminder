from abc import ABC, abstractmethod


class Detector(ABC):

    @property
    @abstractmethod
    def events_type(self) -> list[str]:
        pass

    @abstractmethod
    def detect(self, event) -> str | None:
        pass
