from ..models.item import Item
from .base_behavior import BaseBehavior


class ImprovingWithAgeBehavior(BaseBehavior):
    """Behavior for items that increase in quality as they age (e.g., Aged Brie)."""

    @staticmethod
    def update_quality(item: Item) -> None:
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1
