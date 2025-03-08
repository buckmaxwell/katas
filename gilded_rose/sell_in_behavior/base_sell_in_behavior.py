from abc import ABC, abstractmethod
from ..models.item import Item


class BaseSellInBehavior(ABC):
    """Abstract base class for all quality behaviors."""

    @staticmethod
    @abstractmethod
    def update_sell_in(item: Item) -> None:
        """Updates the quality of an item."""
        pass
