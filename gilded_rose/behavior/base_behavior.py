from abc import ABC, abstractmethod
from ..models.item import Item


class BaseBehavior(ABC):
    """Abstract base class for all quality behaviors."""

    @staticmethod
    @abstractmethod
    def update_quality(item: Item) -> None:
        """Updates the quality of an item."""
        pass
